Highcharts.chart('container', {
    chart: {
        type: 'line'
    },
    title: {
        text: 'Cantidad de Actividades por Día'
    },
    xAxis: {
        type: 'datetime',
        title: {
            text: 'Fecha'
        }
    },
    yAxis: {
        title: {
            text: 'Cantidad de Actividades'
        }
    },
    series: [{
        name: 'Actividades',
        data: [] // lo rellenaremos con fetch
    }]
});


fetch("http://127.0.0.1:5000/get-stats-data")
  .then((response) => response.json())
  .then((data) => {
    const parsedData = data.map((item) => {
      const [year, month, day] = item.date.split("-").map(Number);
      return [Date.UTC(year, month - 1, day), item.count];
    });

    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );

    chart.series[0].setData(parsedData);
  })
  .catch((error) => console.error("Error al cargar datos de actividades por día:", error));

  
Highcharts.chart('container2', {
  chart: {
      type: 'pie'
  },
  title: {
      text: 'Total de Actividades por Tipo'
  },
  series: [{
      name: 'Tipos de Actividades',
      data: [] // lo rellenamos con fetch
  }]
});

fetch("http://127.0.0.1:5000/get-stats-por-tipo")
  .then((response) => response.json())
  .then((data) => {
    const chart = Highcharts.charts.find(chart => chart && chart.renderTo.id === "container2");
    chart.series[0].setData(data);
  })
  .catch((error) => console.error("Error al cargar datos de tipos:", error));



fetch("/get-stats-por-horario")
  .then(response => response.json())
  .then(data => {
    Highcharts.chart('container3', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Actividades por Mes y Hora'
      },
      xAxis: {
        categories: [
          'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
          'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]
      },
      yAxis: {
        title: {
          text: 'Cantidad de Actividades'
        }
      },
      series: data
    });
  })
  .catch(error => console.error("Error al cargar datos por horario:", error));
