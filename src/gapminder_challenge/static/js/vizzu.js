function drawBarChart(data_json) {
  let region_data = [];
  let data_keys = Object.keys(data_json);
  let region_subkeys = Object.keys(data_json[data_keys[0]]);
  let region_size = Object.keys(data_json[data_keys[0]]).length;

  for (let i = 0; i < region_size; i++) {
    let region_data_temp = [];
    for (let j = 0; j < data_keys.length; j++) {
      region_data_temp.push(data_json[data_keys[j]][region_subkeys[i]]);
    }
    region_data.push(region_data_temp);
  }

  let data = {
    series: [
      { name: "Region", type: "dimension" },
      { name: "Year", type: "dimension" },
      { name: "CO2", type: "measure" },
    ],
    records: region_data,
  };
  // console.log(data);

  // export default data;

  let chart = new window.vizzuFromModule("vizzu_card_1", { data });

  let actYear = "";
  let anim = chart.initializing;

  function drawYear(event) {
    event.renderingContext.font = "200 40px Roboto";
    event.renderingContext.fillStyle = "#737373FF";
    // year text position
    event.renderingContext.fillText(actYear, 550, 450);
  }

  function fixMarkerLabel(event) {
    const cutAfterDot = /\..*/;
    let label = event.data.text;
    label = label.replace(cutAfterDot, "");
    event.renderingContext.fillText(
      label,
      event.data.rect.pos.x,
      event.data.rect.pos.y
    );
    event.preventDefault();
  }

  anim = anim.then((chart) => {
    chart.on("logo-draw", drawYear);
    chart.on("plot-marker-label-draw", fixMarkerLabel);
    return chart;
  });

  for (let year = 1898; year <= 2014; year = year + 4) {
    let start_delay = year === 1902 ? 2.5 : 0;
    anim = anim.then((chart) => {
      actYear = year;
      return chart.animate(
        {
          data: {
            filter: (record) => parseInt(record.Year) == year,
          },
          config: {
            channels: {
              y: { set: ["Region"] },
              x: { set: ["CO2"] },
              label: { set: ["CO2"] },
              color: { attach: ["Region"] },
            },
            title: "How Asian became the world largest CO2 emiters",
            sort: "byValue",
          },
          style: {
            fontSize: 12,
            title: {
              fontWeight: 200,
            },
            plot: {
              paddingLeft: 100,
              yAxis: {
                color: "#ffffff00",
                label: {},
              },
              xAxis: {
                title: { color: "#ffffff00" },
                label: { color: "#ffffff00", numberFormat: "grouped" },
              },
              marker: {
                colorPalette:
                  "#b74c20FF #c47f58FF #1c9761FF #ea4549FF #875792FF #3562b6FF #ee7c34FF #efae3aFF",
              },
            },
          },
        },
        {
          duration: 0.6,
          delay: start_delay,
          x: { easing: "linear", delay: 0 },
          y: { delay: 0 },
          show: { delay: 0 },
          hide: { delay: 0 },
          title: { duration: 0, delay: 0 },
        }
      );
    });
  }
}

function drawLineChart(data_json, title, vizzu_id) {
  let line_data = [];
  let data_keys = Object.keys(data_json);
  let data_subkeys = Object.keys(data_json[data_keys[0]]);
  let data_size = Object.keys(data_json[data_keys[0]]).length;

  for (let i = 0; i < data_size; i++) {
    let line_data_temp = [];
    for (let j = 0; j < data_keys.length; j++) {
      line_data_temp.push(data_json[data_keys[j]][data_subkeys[i]]);
    }
    line_data.push(line_data_temp);
  }

  let label_1 = data_keys[0].replace(/_/g, " ");
  let label_2 = data_keys[1].replace(/_/g, " ");
  let label_3 = data_keys[2].replace(/_/g, " ");
  
  // convert to title case
  label_1 = label_1.toLowerCase().replace(/\b(\w)/g, (s) => s.toUpperCase());
  label_2 = label_2.toLowerCase().replace(/\b(\w)/g, (s) => s.toUpperCase());
  label_3 = label_3.toLowerCase().replace(/\b(\w)/g, (s) => s.toUpperCase());


  let data = {
    series: [
      { name: label_1, type: "dimension" },//income
      { name: label_2, type: "dimension" },//year
      { name: label_3, type: "measure" },//children
    ],
    records: line_data,
  };
  // console.log(data);

  // export default data;

  let chart = new window.vizzuFromModule(vizzu_id, { data });

  let actYear = "";
  let anim = chart.initializing;

  function drawYear(event) {
    event.renderingContext.font = "200 40px Roboto";
    event.renderingContext.fillStyle = "#737373FF";
    // year text position
    event.renderingContext.fillText(actYear, 550, 450);
  }

  function fixMarkerLabel(event) {
    const cutAfterDot = /\..*/;
    let label = event.data.text;
    label = label.replace(cutAfterDot, "");
    event.renderingContext.fillText(
      label,
      event.data.rect.pos.x,
      event.data.rect.pos.y
    );
    event.preventDefault();
  }

  anim = anim.then((chart) => {
    chart.on("logo-draw", drawYear);
    chart.on("plot-marker-label-draw", fixMarkerLabel);
    return chart;
  });

  for (let year = 1907; year <= 2018; year = year + 1) {
    let start_delay = year === 1908 ? 2.5 : 0;
    anim = anim.then((chart) => {
      actYear = year;
      return chart.animate(
        {
          data: {
            filter: (record) => parseInt(record.Year) <= year,
          },
          config: {
            channels: {
              x: { set: [label_2] },
              y: {
                set: [label_3],
                // range: {
                //   min: 0,
                //   max: 8,
                // },
              },
              color: { attach: [label_1] },
            },
            title: title,
            geometry: "line",
          },
          style: {
            fontSize: 12,
            title: {
              fontWeight: 200,
            },
            plot: {
              paddingLeft: 0,
              yAxis: {
                color: "#ffffff00",
                label: {},
              },
              xAxis: {
                title: { color: "#ffffff00" },
                label: { color: "#ffffff00", numberFormat: "grouped" },
              },
              marker: {
                colorPalette:
                  "#b74c20FF #c47f58FF #1c9761FF #ea4549FF #875792FF #3562b6FF #ee7c34FF #efae3aFF",
              },
            },
          },
        },
        {
          duration: 0.1,
          delay: start_delay,
          x: { easing: "linear", delay: 0 },
          y: { easing: "linear", delay: 0, duration: 0 },
          show: { delay: 0 },
          hide: { delay: 0 },
          title: { duration: 0, delay: 0 },
        }
      );
    });
  }
}

