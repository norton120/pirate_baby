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
<h1>Brooks Law Model - Cycle Time Calculator</h1>

<!-- Form for adding user requests -->
<div id="input-form" class="input-container">
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
        <label for="teamSize" class="inline-label">Team Size:</label>
        <input type="number" id="teamSize" class="input-field" min="1" value="10" required>
        <div class="prominent-button-wrapper">
            <button type="button" class="prominent-button" onclick="addRequest()">Add Request</button>
        </div>
    </div>
</div>

<!-- Project complexity selection -->
<div id="project-complexity" class="input-container">
    <label for="projectComplexity" class="inline-label">Project Complexity:</label>
    <select id="projectComplexity" class="input-field">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5" selected>5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
    </select>
</div>

<!-- File upload for CSV or Excel -->
<div id="file-upload" class="input-container">
    <label for="fileInput" class="inline-label">Upload CSV or Excel file:</label>
    <input type="file" id="fileInput" class="input-field" accept=".csv, .xlsx, .xls">
    <button type="button" onclick="uploadFile()">Upload</button>
    <a href="#" onclick="downloadStarterCSV()">Download Starter CSV</a>
</div>

<!-- Display user requests -->
<div id="user-requests">
    <h2>User Requests</h2>
    <table>
        <thead>
            <tr>
                <th>Date Requested</th>
                <th>Date Completed</th>
                <th>Team Size</th>
            </tr>
        </thead>
        <tbody id="user-requests-body">
            <!-- Rows will be added here -->
        </tbody>
    </table>
</div>

<button onclick="submitData()">Submit</button>

<!-- Container for displaying the chart -->
<div class="chart-container">
    <canvas id="cycleTimeChart"></canvas>
    <div class="placeholder-text">No results</div>
</div>

<script>
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

    // Brooks Law Model (same as the one from your code)
    class BrooksLawModel {
        constructor(projectComplexity) {
            this.projectComplexity = projectComplexity;
            this.alpha = 0.5; // Scales initial disruption
            this.beta = 1.5; // Scales onboarding duration
            this.gamma = 10; // Fixed recovery contribution per hire
        }

        onboardingDuration(teamSize) {
            return this.beta * this.projectComplexity * Math.log(teamSize);
        }

        cycleTime(time, teamSize, baselineCycleTime) {
            const tauOnboard = this.onboardingDuration(teamSize);
            const tInflection = 0.75 * tauOnboard;
            const k = 1 / tauOnboard;

            const deltaCtInitial = this.alpha * (teamSize + 1) * this.projectComplexity;
            const fRise = deltaCtInitial * Math.exp(-time / tauOnboard);

            const deltaCtRecovery = this.gamma;
            const fRecovery = deltaCtRecovery / (1 + Math.exp(-k * (time - tInflection)));

            return baselineCycleTime + fRise - fRecovery;
        }

        calculateCycleTimes(userRequests) {
            if (!userRequests || userRequests.length === 0) return [];

            const firstRequest = userRequests[0];
            const firstRequestedDate = new Date(firstRequest.dateRequested);
            const firstCompletedDate = new Date(firstRequest.dateCompleted);
            const baselineCycleTime = (firstCompletedDate - firstRequestedDate) / (1000 * 60 * 60 * 24);
            const initialTeamSize = firstRequest.teamSize;

            return userRequests.map((request, index) => {
                const dateRequested = new Date(request.dateRequested);
                const dateCompleted = new Date(request.dateCompleted);
                const rawCycleTime = (dateCompleted - dateRequested) / (1000 * 60 * 60 * 24);

                let expectedCycleTime = null;
                if (index > 0) {
                    const timeSinceFirstRequest = (dateRequested - firstRequestedDate) / (1000 * 60 * 60 * 24);
                    expectedCycleTime = this.cycleTime(timeSinceFirstRequest, initialTeamSize, baselineCycleTime);
                }

                return {
                    teamSize: request.teamSize,
                    rawCycleTime,
                    expectedCycleTime
                };
            });
        }
    }

    let userRequests = [];
    let model;

    // Function to add a request to the form
    function addRequest() {
        const dateRequested = document.getElementById('dateRequested').value;
        const dateCompleted = document.getElementById('dateCompleted').value;
        const teamSize = document.getElementById('teamSize').value;

        if (dateRequested && dateCompleted && teamSize) {
            userRequests.push({
                dateRequested,
                dateCompleted,
                teamSize: Number(teamSize)
            });

            // Clear inputs
            document.getElementById('dateRequested').value = '';
            document.getElementById('dateCompleted').value = '';
            document.getElementById('teamSize').value = '';

            // Update user requests table
            const tbody = document.getElementById('user-requests-body');
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${dateRequested}</td>
                <td>${dateCompleted}</td>
                <td>${teamSize}</td>
            `;
            tbody.appendChild(row);
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
            const teamSize = item['Team Size'];

            if (dateRequested && dateCompleted && teamSize) {
                userRequests.push({
                    dateRequested,
                    dateCompleted,
                    teamSize: Number(teamSize)
                });

                // Update user requests table
                const tbody = document.getElementById('user-requests-body');
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${dateRequested}</td>
                    <td>${dateCompleted}</td>
                    <td>${teamSize}</td>
                `;
                tbody.appendChild(row);
            }
        });
    }

    // Function to download starter CSV
    function downloadStarterCSV() {
        const csvContent = "data:text/csv;charset=utf-8,"
            + "Date Requested,Date Completed,Team Size\n";
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
        const projectComplexity = document.getElementById('projectComplexity').value;
        model = new BrooksLawModel(Number(projectComplexity));

        if (userRequests.length >= 5) {
            const cycleTimes = model.calculateCycleTimes(userRequests);

            // Prepare chart data
            const chartData = {
                labels: cycleTimes.map((_, i) => i), // Use index as x-axis
                datasets: [
                    {
                        label: 'Actual Cycle Time (Days)',
                        data: cycleTimes.map(c => c.rawCycleTime),
                        borderColor: 'rgb(255, 99, 132)',
                        fill: false,
                    },
                    {
                        label: 'Expected Cycle Time (Days)',
                        data: cycleTimes.map(c => c.expectedCycleTime),
                        borderColor: 'rgb(75, 192, 192)',
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
            alert("Please add at least 5 user requests before submitting!");
        }
    }
</script>

<style>
    .input-container {
        padding: .5rem;
        border-radius: .25rem;
        margin-bottom: 20px;
    }
    .input-container:first-of-type {
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
        justify-content: space-between;
    }
    .date-field {
        flex: 1;
        margin-right: 10px;
    }
    .date-field:last-child {
        margin-right: 0;
    }
    @media (max-width: 768px) {
        .date-fields {
            flex-direction: column;
        }
        .date-field {
            margin-right: 0;
        }
    }
</style>
