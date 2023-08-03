function cadastrarUsuario() {
    const nome = document.getElementById('nome').value;
    const sobrenome = document.getElementById('sobrenome').value;
    const email = document.getElementById('email').value;
    const cep = document.getElementById('cep').value;
  
    fetch(`https://viacep.com.br/ws/${cep}/json/`)
      .then(response => response.json())
      .then(data => preencherEndereco(data));
}
  
function preencherEndereco(data) {
    document.getElementById('rua').value = data.logradouro;
    document.getElementById('bairro').value = data.bairro;
    document.getElementById('cidade').value = data.localidade;
    document.getElementById('estado').value = data.uf;
}
  
document.getElementById('cadastroForm').addEventListener('submit', function(event) {
    event.preventDefault();
    cadastrarUsuario();
});
  
document.getElementById('cep').addEventListener('input', function(event) {
    const cep = event.target.value.replace(/\D/g, '');
    if (cep.length === 8) {
      cadastrarUsuario();
    }
});  
