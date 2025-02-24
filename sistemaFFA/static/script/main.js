$(document).ready(function () {
    $('#btn-menu').click(function () {
        $('#menu-mobile').css('transform', 'translateX(0)');
        $('#overlay-menu').css('display', 'block');
    });

    $('#btn-fechar').click(function () {
        $('#menu-mobile').css('transform', 'translateX(-100%)');
        $('#overlay-menu').css('display', 'none');
    });

    $('#overlay-menu').click(function () {
        $('#menu-mobile').css('transform', 'translateX(-100%)');
        $('#overlay-menu').css('display', 'none');
    });
});