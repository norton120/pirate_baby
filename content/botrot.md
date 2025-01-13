---
title: "Bot Rot Detector"
menus: 'main'
layout: "single"
comments: false
hideTitle: true
ShowReadingTime: false
url: "/bot-rot"
summary: Is your code infected with bot rot?
---

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.16.9/xlsx.full.min.js"></script>
<h1>Is Your Software Improving?</h1>

<!-- Form for setting team size for the last 18 months -->
<div id="team-size-form" class="input-container">
    <h3>Set Team Size for the Last 18 Months</h3>
    <div class="table-container">
        <table class="team-size-table">
            <tbody id="team-size-fields">
                <!-- Fields will be added here by JavaScript -->
            </tbody>
        </table>
    </div>
</div>

<!-- Form for adding user requests -->
<div id="input-form" class="input-container">
    <h3>Add Software Requests</h3>
    <h4>Enter each request and click "add request"</h4>
    <div class="input-group">
        <div class="date-fields">
            <div class="date-field">
                <label for="dateRequested" class="inline-label">Date Requested:</label>
                <input type="date" id="dateRequested" class="input-field" required>
            </div>
            <div class="date-field">
                <label for="dateCompleted" class="inline-label">Date Completed:</label>
                <input type="date" id="dateCompleted" class="input-field" required>
            </div>
        </div>
    </div>
    <div class="request-note">
        <label for="note" class="label">Note (optional):</label><br/>
        <textarea id="note" placeholder="i.e. requested new button"></textarea>
    </div>
    <div class="prominent-button-wrapper">
        <button type="button" class="prominent-button" onclick="addRequest()">Add Request</button>
    </div>
    <div id="file-upload">
        <h4>...or upload a spreadsheet of software requests</h4>
        <label for="fileInput" class="label">Upload CSV or Excel file:</label>
        <input type="file" id="fileInput" class="input-field" accept=".csv, .xlsx, .xls">
        <button type="button" onclick="uploadFile()">Upload</button>
        <div>
            Download a
            <a href="#" onclick="downloadStarterCSV()">sample spreadsheet</a>
            for help getting started.
        </div>
    </div>
</div>

<!-- Display user requests -->
<div id="user-requests" style="display: none;">
    <h3>Software Requests</h3>
    <table>
        <thead>
            <tr>
                <th>Date Requested</th>
                <th>Date Completed</th>
            </tr>
        </thead>
        <tbody id="user-requests-body">
            <!-- Rows will be added here -->
        </tbody>
    </table>
</div>

<!-- Container for displaying the chart -->
<div class="chart-container">
    <canvas id="cycleTimeChart"></canvas>
    <div class="placeholder-text">No results</div>
</div>

<style>
    .input-container {
        padding: .5rem;
        border-radius: .25rem;
        margin-bottom: 20px;
        border: thin solid #777777;
    }
    .input-field {
        display: inline-block;
        margin-top: 5px;
        margin-bottom: 10px;
        padding: 8px;
        width: calc(100% - 150px);
        box-sizing: border-box;
    }
    .inline-label {
        display: inline-block;
        width: 140px;
        text-align: right;
        margin-right: 10px;
    }
    .dark .input-field {
        background-color: #333;
        color: #fff;
        border: 1px solid #555;
    }
    .input-field:focus {
        outline: none;
        border-color: #007bff;
    }
    .prominent-button-wrapper {
        width: 100%;
        text-align: right;
    }
    .prominent-button {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        font-size: 16px;
        border-radius: 5px;
    }
    .prominent-button:hover {
        background-color: #0056b3;
    }
    .chart-container {
        position: relative;
        width: 100%;
        height: 400px;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
    }
    .placeholder-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #999;
        font-size: 24px;
        pointer-events: none;
    }
    .date-fields {
        display: flex;
        margin: auto;
    }
    .date-fields input {
        border: 1px solid #ccc;
        border-radius: .25rem;
    }
    textarea {
        border: 1px solid #ccc;
        border-radius: .25rem;
    }
    .date-field * {
        margin: auto;
        display: inline;
    }
    .table-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .team-size-table {
        width: 100%;
        border-collapse: collapse;
    }
    .team-size-table td {
        border: 1px solid #ccc;
        padding: 8px;
        text-align: center;
        vertical-align: top;
    }
    .editable-div {
        width: 100%;
        height: 100%;
        padding: 8px;
        box-sizing: border-box;
        text-align: center;
        border: 1px solid #ccc;
        background-color: #fff;
        cursor: text;
    }
    .editable-div:empty:before {
        content: attr(placeholder);
        color: #999;
    }
    .grayed-out {
        background-color: #e0e0e0;
        pointer-events: none;
    }
</style>

<script>

class BrooksLawCalculator {
    constructor(onboardingMonths = 2) {
        this.onboardingMonths = onboardingMonths; // The duration for onboarding in months
    }

    // Calculate fully realized output based on the number of team members
    getFullyRealizedOutputPercentage(teamSize) {
        if (teamSize < 1) return 0;
        let totalOutput = 100 * teamSize; // Raw contribution per member
        let handicap = 5 * (teamSize * (teamSize - 1)) / 2; // 5% handicap per edge in the graph
        return totalOutput - handicap;
    }

    // Calculate productivity per team member during onboarding
    getOnboardingOutputProgress(month) {
        return Math.min(1, month / this.onboardingMonths); // Linearly increases to 1
    }

    // Calculate cycle time based on changes in team size over time
    calculateCycleTime(monthlyData, initialCycleTime=5) {
        let cycleTime = initialCycleTime; // cycle time in days
        let effectiveTeamSize = null;
        let month = 0;
        let baselinePercent = null;
        const cycleTimes = []; // Array to store cycle times for plotting

        // Process the monthly data from monthlyData
        for (let [monthYear, newTeamSize] of Object.entries(monthlyData)) {
            month++;
            if (effectiveTeamSize === null) {
                if (newTeamSize === null) {
                    continue;
                }
                effectiveTeamSize = newTeamSize;
            }
            if (newTeamSize === null) {
                newTeamSize = effectiveTeamSize;
            }
            const onboardingNewMembers = Math.max(0, newTeamSize - effectiveTeamSize);
            const currentFullyRealizedOutputPercentage = this.getFullyRealizedOutputPercentage(effectiveTeamSize);

            if (baselinePercent == null) {
                baselinePercent = currentFullyRealizedOutputPercentage;
            }

            const newMemberOutputPercentage = onboardingNewMembers > 0
                ? this.getFullyRealizedOutputPercentage(onboardingNewMembers) * this.getOnboardingOutputProgress(month)
                : 0;

            // Handicapping the team during onboarding of new members
            const handicap = onboardingNewMembers * 5; // Reduction per existing member

            const totalOutput = currentFullyRealizedOutputPercentage + newMemberOutputPercentage;
            const adjustedOutput = totalOutput - handicap;

            const ratio = (initialCycleTime / baselinePercent);
            cycleTime = initialCycleTime - (ratio * adjustedOutput)
            // cycleTime = cycleTime / (adjustedOutput / 100); // Adjust the cycle time accordingly

            // Apply 1% efficiency gain per month
            cycleTime *= 0.99;

            // Minimum cycle time is 1 day
            //cycleTime = Math.max(1, cycleTime);

            // Record the cycle time for plotting
            cycleTimes.push({ month: monthYear, cycleTime: cycleTime });

            // Update the effective team size for the next period
            effectiveTeamSize = newTeamSize;
        }

        return cycleTimes;
    }
}

class ActualCycleTimeCalculator {
    /* takes an array of objects with the following structure:
        {
            dateRequested: "2021-01-01",
            dateCompleted: "2021-01-05",
            note: "Some note",
        }
        calculates the aggreated average cycle time for each month
        and returns an array of objects with the following structure:
        {
            month: "2021-01",
            cycleTime: 3.5
        }
    */
    calculateCycleTimes(userRequests) {
        if (!userRequests || userRequests.length === 0) return [];
        let cycleTimes = [];
        userRequests.map((request, index) => {
            const dateRequested = new Date(request.dateRequested);
            const dateCompleted = new Date(request.dateCompleted);
            const rawCycleTime = (dateCompleted - dateRequested) / (1000 * 60 * 60 * 24);
            cycleTimes.push({ month: dateRequested.toISOString().slice(0, 7), cycleTime: rawCycleTime });
        });

        // aggregate cycle times by month
        let aggregatedCycleTimes = {};

        cycleTimes.forEach((cycleTime) => {
            // average cycle time for the month
            if (aggregatedCycleTimes[cycleTime.month]) {
                aggregatedCycleTimes[cycleTime.month].push(cycleTime.cycleTime);
            } else {
                aggregatedCycleTimes[cycleTime.month] = [cycleTime.cycleTime];
            }
        });
        // calculate the average cycle time for each month, rounded to 2 decimal places
        let averageCycleTimes = {};
        aggregatedCycleTimes.forEach((month, cycleTimes) => {
            averageCycleTimes[month] = cycleTimes.reduce((a, b) => a + b, 0) / cycleTimes.length;
            averageCycleTimes[month] = Math.round(averageCycleTimes[month] * 100) / 100;
        });
        return averageCycleTimes;
    }
}

// Apply theme based on preference
if (localStorage.getItem("pref-theme") === "dark") {
    document.body.classList.add('dark');
} else if (localStorage.getItem("pref-theme") === "light") {
    document.body.classList.remove('dark');
} else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.body.classList.add('dark');
}

// Function to render the chart
let chart;
let softwareRequests = [];
let teamSizes = {};
const chartConfig = {
    type: 'line',
    data: {
        labels: [], // dates or time
        datasets: [
            {
                label: 'Actual Cycle Time (Days)',
                borderColor: 'rgb(255, 99, 132)',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: false,
                data: []
            },
            {
                label: 'Expected Cycle Time (Days)',
                borderColor: 'rgb(75, 192, 192)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: false,
                data: []
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                type: 'linear', // x-axis with a numeric scale (days from start)
                position: 'bottom'
            }
        }
    }
};

const ctx = document.getElementById('cycleTimeChart').getContext('2d');

let model;

// Function to add a request to the form
function addRequest() {
    const dateRequested = document.getElementById('dateRequested').value;
    const dateCompleted = document.getElementById('dateCompleted').value;
    const note = document.getElementById('note').value;

    if (dateRequested && dateCompleted && teamSizes) {
        const request = {
            dateRequested,
            dateCompleted,
            note
        };
        softwareRequests.push(request);

        // Clear inputs
        document.getElementById('dateRequested').value = '';
        document.getElementById('dateCompleted').value = '';
        document.getElementById('note').value = '';

        // Update user requests table
        const tbody = document.getElementById('user-requests-body');
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${dateRequested}</td>
            <td>${dateCompleted}</td>
            <td>${note}</td>
        `;
        tbody.appendChild(row);

        // Toggle visibility of the Software Requests block
        toggleSoftwareRequestsVisibility();

        // Submit data to update the chart
        submitData();
    } else {
        alert("Please fill all fields!");
    }
}

// Function to handle file upload
function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const data = event.target.result;
            if (file.name.endsWith('.csv')) {
                Papa.parse(data, {
                    header: true,
                    complete: function(results) {
                        processFileData(results.data);
                    }
                });
            } else if (file.name.endsWith('.xlsx') || file.name.endsWith('.xls')) {
                const workbook = XLSX.read(data, { type: 'binary' });
                const sheetName = workbook.SheetNames[0];
                const sheet = workbook.Sheets[sheetName];
                const json = XLSX.utils.sheet_to_json(sheet);
                processFileData(json);
            }
        };
        reader.readAsBinaryString(file);
    } else {
        alert("Please select a file to upload!");
    }
}

// Function to process file data and add to user requests
function processFileData(data) {
    data.forEach(item => {
        const dateRequested = item['Date Requested'];
        const dateCompleted = item['Date Completed'];
        const note = item['Note'];

        if (dateRequested && dateCompleted) {
            const request = {
                dateRequested,
                dateCompleted,
                note
            };
            softwareRequests.push(request);

            // Update user requests table
            const tbody = document.getElementById('user-requests-body');
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${dateRequested}</td>
                <td>${dateCompleted}</td>
                <td>${note}</td>
            `;
            tbody.appendChild(row);
        }
    });

    // Toggle visibility of the Software Requests block
    toggleSoftwareRequestsVisibility();

    // Submit data to update the chart
    submitData();
}

// Function to download starter CSV
function downloadStarterCSV() {
    const csvContent = "data:text/csv;charset=utf-8,"
        + "Date Requested,Date Completed,Note\n";
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "starter.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Function to submit data and plot the chart
function submitData() {
    const model = new BrooksLawCalculator();
    const expectedCycleTimes = model.calculateCycleTime(teamSizes);
    console.log(expectedCycleTimes)
    if (softwareRequests.length >= 5) {
        const actualCycleTimeCalculator = new ActualCycleTimeCalculator();
        const actualCycleTimes = actualCycleTimeCalculator.calculateCycleTimes(softwareRequests);

        // Prepare chart data
        const chartData = {
            labels: expectedCycleTimes.map(c => c.month), // Use month as x-axis
            datasets: [
                {
                    label: 'Expected Cycle Time (Days)',
                    data: expectedCycleTimes.map(c => c.cycleTime),
                    borderColor: 'rgb(75, 192, 192)',
                    fill: false,
                },
                {
                    label: 'Actual Cycle Time (Days)',
                    data: actualCycleTimes.map(c => c.cycleTime),
                    borderColor: 'rgb(255, 99, 132)',
                    fill: false,
                }
            ]
        };

        // Update chart with data
        if (chart) {
            chart.destroy();
        }
        chart = new Chart(ctx, {
            ...chartConfig,
            data: chartData
        });

        // Hide placeholder text
        document.querySelector('.placeholder-text').style.display = 'none';
    } else {
        // just generate the chart for the BrooksLawCaclulator based on the teamSizes
        const actualCycleTimeCalculator = new ActualCycleTimeCalculator();

        // Prepare chart data
        const chartData = {
            labels: expectedCycleTimes.map(c => c.month), // Use month as x-axis
            datasets: [
                {
                    label: 'Expected Cycle Time (Days)',
                    data: expectedCycleTimes.map(c => c.cycleTime),
                    borderColor: 'rgb(75, 192, 192)',
                    fill: false,
                },
            ]
        };

        // Update chart with data
        if (chart) {
            chart.destroy();
        }
        chart = new Chart(ctx, {
            ...chartConfig,
            data: chartData
        });

        // Hide placeholder text
        document.querySelector('.placeholder-text').style.display = 'none';

    }
}

    // Watch for changes in teamSizes and softwareRequests and update the chart
    const teamSizesProxy = new Proxy(teamSizes, {
        set(target, property, value) {
            target[property] = value;
            submitData();
            return true;
        }
    });

    const softwareRequestsProxy = new Proxy(softwareRequests, {
        set(target, property, value) {
            target[property] = value;
            submitData();
            return true;
        }
    });

    // Generate fields for the last 18 months
    function generateTeamSizeFields() {
        const container = document.getElementById('team-size-fields');
        const currentDate = new Date();
        let row = document.createElement('tr');
        for (let i = 0; i < 18; i++) {
            const date = new Date(currentDate.getFullYear(), currentDate.getMonth() - i, 1);
            const monthYear = date.toISOString().slice(0, 7);
            const month = date.toLocaleString('default', { month: 'short' });
            const year = date.getFullYear().toString().slice(-2);

            if (i > 0 && i % 6 === 0) {
                container.appendChild(row);
                row = document.createElement('tr');
            }

            const cell = document.createElement('td');
            cell.innerHTML = `<div>${month}-${year}</div><div contenteditable="true" id="teamSize-${monthYear}" class="editable-div" placeholder="5" oninput="updateTeamSizes('${month}-${year}', this.textContent)"></div>`;
            row.appendChild(cell);
            updateTeamSizes(`${month}-${year}`, "")
        }
        container.appendChild(row);
    }

    // Function to update team sizes
    function updateTeamSizes(monthYear, value) {
        teamSizesProxy[monthYear] = value.trim() === "" ? null : parseInt(value, 10);
    }

    // Function to toggle the visibility of the Software Requests block
    function toggleSoftwareRequestsVisibility() {
        const userRequestsDiv = document.getElementById('user-requests');
        if (softwareRequests.length > 0) {
            userRequestsDiv.style.display = 'block';
        } else {
            userRequestsDiv.style.display = 'none';
        }
    }

    // Call the function to generate fields on page load
    document.addEventListener('DOMContentLoaded', generateTeamSizeFields);
</script>
