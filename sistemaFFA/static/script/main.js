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

$(".excluirTransacao").click(function (event) {
    event.preventDefault();
    const dataUrl = $(this).data("url");

    $.ajax({
        url: dataUrl,
        method: "get",
        success: (response) => {
            $("#transacaoModal .modal-footer").html(response);
        }
    });
});

$(".excluirContato").click(function (event) {
    event.preventDefault();
    const dataUrl = $(this).data("url");

    $.ajax({
        url: dataUrl,
        method: "get",
        success: (response) => {
            $("#contatoModal .modal-footer").html(response);
        }
    });
});

$(".excluirCategoria").click(function (event) {
    event.preventDefault();
    const dataUrl = $(this).data("url");

    $.ajax({
        url: dataUrl,
        method: "get",
        success: (response) => {
            $("#categoriaModal .modal-footer").html(response);
        }
    });
});