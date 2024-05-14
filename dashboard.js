document.addEventListener('DOMContentLoaded', function () {
    // Progress Tracking Chart
    const ctx = document.getElementById('progressChart').getContext('2d');
    const progressChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Object.keys(dailyProgress),
            datasets: [{
                label: 'Daily Progress Entries',
                data: Object.values(dailyProgress),
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 1,
                fill: true,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
