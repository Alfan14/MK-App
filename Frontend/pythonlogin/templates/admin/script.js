document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('insightsChart').getContext('2d');
    var insightsChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['5k', '10k', '15k', '20k', '25k', '30k', '35k', '40k', '45k', '50k', '55k', '60k'],
            datasets: [{
                label: 'User Insights',
                data: [20, 40, 60, 80, 100, 80, 60, 80, 100, 80, 60, 40],
                borderColor: '#007bff',
                backgroundColor: 'rgba(0, 123, 255, 0.1)',
                fill: true
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
