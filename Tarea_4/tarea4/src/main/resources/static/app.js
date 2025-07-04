document.addEventListener('DOMContentLoaded', () => {
  cargarActividades();
});

function cargarActividades() {
  fetch('/api/actividades/finalizadas')
    .then(res => res.json())
    .then(data => renderTabla(data))
    .catch(console.error);
}

function renderTabla(actividades) {
  const tbody = document.querySelector('#tabla-actividades tbody');
  tbody.innerHTML = '';
  actividades.forEach(a => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${a.nombre}</td>
      <td>${a.tema}</td>
      <td>${a.inicio}</td>
      <td>${a.termino}</td>
      <td>${a.region}</td>
      <td>${a.comuna}</td>
      <td>${a.sector}</td>
      <td class="nota" data-id="${a.id}">${a.notaPromedio}</td>
      <td><img src="${a.foto}" width="50"></td>
      <td><button onclick="evaluar(${a.id})">Evaluar</button></td>
    `;
    tbody.appendChild(tr);
  });
}

function evaluar(actividadId) {
  let valor = prompt('Ingrese nota (1 a 7):');
  if (!valor || isNaN(valor)) return alert('Debe ser un número válido');
  valor = parseInt(valor);
  if (valor < 1 || valor > 7) return alert('Nota fuera de rango (1-7)');

  fetch('/api/notas', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({actividadId, nota: valor})
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) return alert(data.error);
      document.querySelector(`.nota[data-id="${actividadId}"]`).textContent = data.nuevoPromedio;
    })
    .catch(err => alert('Error al enviar nota'));
}