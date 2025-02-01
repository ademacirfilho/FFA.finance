var ctx = document.getElementById('chart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['out/2024', 'nov/2024'],
        datasets: [{
            label: 'Receitas',
            data: [0, 0],
            backgroundColor: 'rgba(38, 198, 218, 0.1)',
            borderColor: 'rgba(38, 198, 218, 1)',
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

document.getElementById('btn-menu').addEventListener('click', function () {
    document.getElementById('menu-mobile').style.transform = 'translateX(0)';
    document.getElementById('overlay-menu').style.display = 'block';
});
document.getElementById('btn-fechar').addEventListener('click', function () {
    document.getElementById('menu-mobile').style.transform = 'translateX(-100%)';
    document.getElementById('overlay-menu').style.display = 'none';
});
document.getElementById('overlay-menu').addEventListener('click', function () {
    document.getElementById('menu-mobile').style.transform = 'translateX(-100%)';
    document.getElementById('overlay-menu').style.display = 'none';
});