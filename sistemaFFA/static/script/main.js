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

$(document).ready(function () {
    $('.btn-custom').click(function () {
        var $btn = $(this);
        $('.btn-custom').removeClass('active');
        $btn.addClass('active').prop('disabled', true);

        var category = $btn.data('category');
        const filtrarCategoriasURL = $('#meu-botao').data('url');

        $('#categorias-partial').html('<div class="spinner">Carregando...</div>');

        $.ajax({
            url: filtrarCategoriasURL,
            type: 'GET',
            data: { category: category },
            success: function (response) {
                $('#categorias-partial').html(response);
            },
            error: function (xhr, status, error) {
                console.error('Erro na requisição AJAX:', status, error);
                console.error('Resposta do servidor:', xhr.responseText);
                $('#categorias-partial').html('<div class="error">Erro ao carregar categorias.</div>');
            },
            complete: function () {
                $btn.prop('disabled', false);
            }
        });
    });
});