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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brooks Law Model - Cycle Times</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Brooks Law Model - Cycle Time Calculator</h1>

    <!-- Form for adding user requests -->
    <div id="input-form">
        <div class="input-group">
            <label for="dateRequested">Date Requested:</label>
            <input type="date" id="dateRequested" required>
            <label for="dateCompleted">Date Completed:</label>
            <input type="date" id="dateCompleted" required>
            <label for="teamSize">Team Size:</label>
            <input type="number" id="teamSize" min="1" required>
            <button type="button" onclick="addRequest()">Add Request</button>
        </div>
    </div>

    <button onclick="submitData()">Submit</button>

    <!-- Container for displaying the chart -->
    <div>
        <canvas id="cycleTimeChart"></canvas>
    </div>

    <script>
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
        let model = new BrooksLawModel(5); // Example complexity 5

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
            } else {
                alert("Please fill all fields!");
            }
        }

        // Function to submit data and plot the chart
        function submitData() {
            if (userRequests.length > 0) {
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
            } else {
                alert("No user requests to submit!");
            }
        }
    </script>
</body>
</html>
