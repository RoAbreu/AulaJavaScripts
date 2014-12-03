 var rest=angular.module('rest', []);
        rest.factory('LivroApi', function($rootScope){
            return{
                salvar: function(livro){
                    var obj={};
                    obj.success=function(fcnSucesso){
                        obj.fcnSucesso=fcnSucesso;
                    };
                    obj.error=function(fcnErro){
                        obj.fcnErro=fcnErro;
                    };
                    setTimeout(function(){
                        livro.id=1;
                        obj.fcnSucesso(livro);
                        $rootScope.$digest();
                    }, 1000);

                    return obj;
                }
            };
        });
