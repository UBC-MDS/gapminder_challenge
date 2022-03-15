  function showStory(event) {
      var card = event.currentTarget.closest(".card");
      // hide card
      card.style.display = "none";
      // show story
      var story = document.getElementById("story");
      story.style.display = "block";

      var myVizzu = document.getElementById("myVizzu");
      myVizzu.style.width = '650px';
      myVizzu.style.height = '600px';
      
      doAnimation();

    }
  
  function doAnimation() {
    var iframe = document.getElementById("iframe_card_1");
    var elmnt = iframe.contentWindow.document.getElementById("vizzu_data");
    var my_array = elmnt.dataset.co2
    var region_json = JSON.parse(my_array);

    var region_data = []
    var region_keys = Object.keys(region_json);
    var region_subkeys = Object.keys(region_json[region_keys[0]])
    var region_size = Object.keys(region_json[region_keys[0]]).length;
    
    

    for (var i = 0; i < region_size; i++) {
      var region_data_temp = []
      for (var j = 0; j < region_keys.length; j++) {
        region_data_temp.push(region_json[region_keys[j]][region_subkeys[i]])
      }
      region_data.push(region_data_temp)
    }

    // console.log(region_json)
    // console.log(region_subkeys);
    // console.log(region_data);

      let data = {
        series: [
          { name: 'Region', type: 'dimension' },
          { name: 'Year', type: 'dimension' },
          { name: 'CO2', type: 'measure' },
        ],
        records: region_data
      };

      // export default data;

      let chart = new window.vizzuFromModule('myVizzu', { data });

      let actYear = '';
      let anim = chart.initializing;

      function drawYear(event) {
        event.renderingContext.font = "200 40px Roboto";
        event.renderingContext.fillStyle = "#737373FF";
        // event.renderingContext.fillText(actYear,
        //   1000, 500);
        event.renderingContext.fillText(actYear,
          550, 500);

      }

      function fixMarkerLabel(event) {
        const cutAfterDot = /\..*/;
        let label = event.data.text;
        label = label.replace(cutAfterDot, '');
        event.renderingContext.fillText(label, event.data.rect.pos.x, event.data.rect.pos.y);
        event.preventDefault();
      }

      anim = anim.then(chart => {
        chart.on('logo-draw', drawYear);
        chart.on('plot-marker-label-draw', fixMarkerLabel);
        return chart;
      });

      for (let year = 1902; year <= 2014; year = year + 4) {
        anim = anim.then(chart => {
          actYear = year;
          return chart.animate({
            data:
            {
              filter: record => parseInt(record.Year) == year
            },
            config: {
              channels: {
                y: { set: ['Region'], },
                x: { set: ['CO2'] },
                label: { set: ['CO2'] },
                color: { attach: ['Region'] }
              },
              title: 'How Asian become largest CO2 emiters in the world',
              sort: 'byValue'
            },
            style:
            {
              fontSize: 12,
              title:
              {
                fontWeight: 200
              },
              plot: {
                paddingLeft: 100,
                // paddingTop: 50,
                yAxis: {
                  color: '#ffffff00',
                  label: {
                    // paddingRight: 20
                  },
                },
                xAxis: {
                  title: { color: '#ffffff00' },
                  label: { color: '#ffffff00', numberFormat: 'grouped' }
                },
                marker: {
                  colorPalette: '#b74c20FF #c47f58FF #1c9761FF #ea4549FF #875792FF #3562b6FF #ee7c34FF #efae3aFF'
                }
              }
            }
          },
            {
              duration: 0.6, delay: 0,
              x: { easing: 'linear', delay: 0 },
              y: { delay: 0 },
              show: { delay: 0 },
              hide: { delay: 0 },
              title: { duration: 0, delay: 0 }
            }
          )
        });
      }
    }
