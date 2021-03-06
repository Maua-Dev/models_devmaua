import pytest
from pydantic import ValidationError

from devmaua.src.enum.tipo_endereco import TipoEndereco

from devmaua.src.models.endereco import Endereco

class Test_Endereco():
    
    def test_create_instance_model(self):
        end = Endereco(logradouro='rua de tal',
                       numero = 20,
                       cep='00000-000',
                       tipo = TipoEndereco.RESIDENCIAL)
        assert end.logradouro == 'rua de tal'
        assert end.numero == 20
        assert end.cep == '00000-000'
        assert end.tipo == TipoEndereco.RESIDENCIAL
        
    def test_validator_error_numero(self):
        with pytest.raises(ValidationError) as error_info:
            end = Endereco(logradouro='rua de tal',
                       numero = -20,
                       cep='00000-000',
                       tipo = TipoEndereco.RESIDENCIAL)
            
    def test_validator_error_cep(self):
        with pytest.raises(ValidationError) as error_info:
            end = Endereco(logradouro='rua de tal',
                       numero = 20,
                       cep='a',
                       tipo = TipoEndereco.RESIDENCIAL)
            
    def test_criar_endereco_por_dict(self):
        d = {
            "logradouro": "rua de tal",
            "numero": 20,
            "cep": "00000-000",
            "complemento": None,
            "tipo": 1
            }
        
        end = Endereco.criarEnderecoPorDict(d)
        
        assert end.logradouro == 'rua de tal'
        assert end.numero == 20
        assert end.cep == '00000-000'
        assert end.tipo == TipoEndereco.RESIDENCIAL
        