var livroModulo=angular.module('livro-modulo', ['livro-servico']);
livroModulo.directive('livroForm', [function(){
    return{
        restrict: 'E',
        templateUrl: '/static/livro/html/livro_form.html',
        scope: {livroSalvo: '&'},
        controller: function($scope, LivroApi){
            $scope.livro = {titulo: 'O Cortiço', preco: '10', autor: 'Aluizio Azevedo'};
            $scope.executandoSalvamento = false;
            $scope.erros = {};
            $scope.salvar = function(){
                $scope.executandoSalvamento = true;
                $scope.erros = {};
                var promessa = LivroApi.salvar($scope.livro);
                promessa.success(function(livro){
                    $scope.executandoSalvamento = false;
                    $scope.livro.titulo='';
                    $scope.livro.autor='';
                    $scope.livro.preco='';
                    if ($scope.livroSalvo != null){
                        $scope.livroSalvo({'livro': livro})
                    }
                });
                promessa.error(function(erros){
                    $scope.erros = erros;
                    $scope.executandoSalvamento = false;

                });
            }
        }
    };
}]);

livroModulo.directive('livroLinha', [function(){
    return{
        restrict: 'A',
        replace: true,
        templateUrl: '/static/livro/html/livro_linha_tabela.html',
        scope: {
            livro: '=',
            livroDeletado: '&'
        },
        controller: function($scope, LivroApi){
            $scope.apagandoFlag = false;
            $scope.editandoFlag = false;
            $scope.livroEdicao = {};
            $scope.deletar = function(){
                $scope.apagandoFlag = true;
                LivroApi.deletar($scope.livro.id).success(function(){
                    $scope.apagandoFlag = false;
                    if ($scope.livroDeletado != null){
                        $scope.livroDeletado();
                    }
                });
            }
            function copiarLivro(origem, destino){
                destino.id = origem.id;
                destino.titulo = origem.titulo;
                destino.preco = origem.preco;
                destino.autor = origem.autor;
            }
            $scope.entrarModoEdicao = function(){
                $scope.editandoFlag = true;
                copiarLivro($scope.livro, $scope.livroEdicao);
            };
            $scope.sairModoEdicao = function(){
                $scope.editandoFlag = false;
            };
            $scope.editar = function(){
                LivroApi.editar($scope.livroEdicao).success(function(livroServidor){
                    copiarLivro(livroServidor, $scope.livro);
                    $scope.editandoFlag = false;
                });
            }
        }
    };
}]);