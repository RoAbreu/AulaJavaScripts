/**
 * Created by roberta on 28/10/2014.
 */
$(document).ready(function () {
    var $livroForm = $('#livro-form');

    $livroForm.hide();
    $('#mostrar-form-btn').click(function () {
        $livroForm.slideToggle();
    });
 //   var $dataInput = $('#dataInput');

    var $tituloInput = $('#tituloInput');
    var $precoInput = $('#precoInput');
    var $autorInput = $('#autorInput');
    var $ajaxGif = $('#ajax-gif');

    var $tituloDiv = $('#tituloDiv');
    var $precoDiv = $ ('#precoDiv');
    var $autorDiv = $ ('#autorDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');
    var $helpTituloSpan = $('#help-titulo');
    var $helpPrecoSpan = $('#help-preco')
    var $helpAutorSpan = $('#help-autor')
    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha=function adicionarLinha(livro) {
        var linha = '<tr id="tr' + livro.id + '"> <td>' + livro.titulo + '</td>' +
            '<td>' + livro.preco + '</td>' +
            '<td>' + livro.autor + '</td>' +
          //  '<td>' + livro.data + '</td>' +
            '<td><button id="bt' + livro.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';

        $corpoTabela.prepend(linha);
        var $linhaHtml = $('#tr' + livro.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();
        $('#bt' + livro.id).click(function () {
            $linhaHtml.fadeOut();
            $.post('/livros/rest/delete',{'livro_id':livro.id}).success(function(){
                $linhaHtml.remove();
            }).error(function(){
                alert('Remoção não funcionou');
                $linhaHtml.fadeIn();
            });
        });
    }

    $.get('/livros/rest').success(function (listaDeLivros) {
        for (var i = 0; i < listaDeLivros.length; i += 1) {
            adicionarLinha(listaDeLivros[i]);
        }
    });

    $salvarBtn.click(function () {
        var livro = {titulo: $tituloInput.val(),
            preco: $precoInput.val(),
        //    data: $dataInput.val()
            autor: $autorInput.val()};

        $ajaxGif.slideDown();
        $salvarBtn.hide();

        var promessa = $.post('/livros/rest/save', livro);
        
        promessa.success(function (livro_do_servidor) {
            console.log(livro_do_servidor);
            adicionarLinha(livro_do_servidor);
        });

       promessa.error(function (erros) {
            if (erros.responseJSON != null && erros.responseJSON.titulo != null) {
                $tituloDiv.addClass('has-error');
                $helpTituloSpan.text(erros.responseJSON.titulo);
            }
            if (erros.responseJSON != null && erros.responseJSON.preco != null) {
                $precoDiv.addClass('has-error');
                $helpPrecoSpan.text(erros.responseJSON.preco);
            }
            if (erros.responseJSON != null && erros.responseJSON.autor != null) {
                $autorDiv.addClass('has-error');
                $helpAutorSpan.text(erros.responseJSON.autor);
            }
        });

        promessa.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
       });
    });