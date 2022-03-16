function flip(event) {
  let element = event.currentTarget.closest(".card");
  if (element.style.transform == "rotateY(180deg)") {
    element.style.transform = "rotateY(0deg)";
  } else {
    element.style.transform = "rotateY(180deg)";
  }
}

function flip_story(event) {
  let card = event.currentTarget.closest(".card");
  let front = card.querySelector(".front");
  let back = card.querySelector(".back");
  let iframe = back.querySelector(".iframe_card");
  let story = card.querySelector(".story");
  let vizzu_canvas = story.querySelector(".vizzu_canvas");
  if (card.style.transform == "rotateY(360deg)") {
    setTimeout(() => {
      front.style.display = "flex";
      story.style.display = "none";
    }, 1000);
    card.style.transform = "rotateY(180deg)";
  } else {
    card.style.transform = "rotateY(360deg)";
    front.style.display = "none";
    story.style.display = "block";
    vizzu_canvas.style.width = "650px";
    vizzu_canvas.style.height = "500px";
    // which one to draw
    if (card.classList.contains("card-1")) {
        let data_card =
          iframe.contentWindow.document.getElementById("data_card_1");
        let data_array = data_card.dataset.card_1_data;
        let data_json = JSON.parse(data_array);
      drawBarChart(data_json);
    } else if (card.classList.contains("card-2")) {
       let data_card =
         iframe.contentWindow.document.getElementById("data_card_2");
       let data_array = data_card.dataset.card_2_data;
       let data_json = JSON.parse(data_array);
      drawLineChart(data_json);
    }
  }
}

function spark_btn(btn) {
  setTimeout(function () {
    btn.style.display = "block";
    btn.classList.add("is-active");
    party.sparkles(btn);
  }, 1500);
}
function shake_btn(btn) {
  btn.classList.add("button-shake");
}

function no_click(event) {
  let element = event.currentTarget.closest(".btn-group");
  element.classList.add("no-click");
}

function quiz1Func(event, id) {
  btn1 = document.getElementById("btn1");
  btn2 = document.getElementById("btn2");
  btn3 = document.getElementById("btn3");
  btn4 = document.getElementById("btn4");

  btn1.style.backgroundColor = "#ED213A";
  btn1.style.color = "white";
  btn2.style.backgroundColor = "#56ab2f"; // correct answer
  btn2.style.color = "white";
  btn3.style.backgroundColor = "#ED213A";
  btn3.style.color = "white";

  spark_btn(btn4);
  if (id == "btn1") {
    shake_btn(btn1);
  } else if (id == "btn3") {
    shake_btn(btn3);
  }
  no_click(event);
}
function quiz2Func(event, id) {
  btn1 = document.getElementById("q2_btn1");
  btn2 = document.getElementById("q2_btn2");
  btn3 = document.getElementById("q2_btn3");
  btn4 = document.getElementById("q2_btn4");

  btn1.style.backgroundColor = "#ED213A";
  btn1.style.color = "white";
  btn2.style.backgroundColor = "#ED213A";
  btn2.style.color = "white";
  btn3.style.backgroundColor = "#56ab2f"; // correct answer is 2.7
  btn3.style.color = "white";

  spark_btn(btn4);
  if (id == "btn1") {
    shake_btn(btn1);
  } else if (id == "btn2") {
    shake_btn(btn2);
  }
  no_click(event);
}

function quiz3Func(event, id) {
  btn1 = document.getElementById("q3_btn1");
  btn2 = document.getElementById("q3_btn2");
  btn3 = document.getElementById("q3_btn3");
  btn4 = document.getElementById("q3_btn4");

  btn1.style.backgroundColor = "#ED213A";
  btn1.style.color = "white";
  btn2.style.backgroundColor = "#ED213A";
  btn2.style.color = "white";
  btn3.style.backgroundColor = "#56ab2f"; // correct answer is 2.7
  btn3.style.color = "white";

  spark_btn(btn4);
  if (id == "btn1") {
    shake_btn(btn1);
  } else if (id == "btn2") {
    shake_btn(btn2);
  }
  no_click(event);
}

function quiz4Func(event, id) {
  btn1 = document.getElementById("q4_btn1");
  btn2 = document.getElementById("q4_btn2");
  btn3 = document.getElementById("q4_btn3");
  btn4 = document.getElementById("q4_btn4");

  btn1.style.backgroundColor = "#ED213A";
  btn1.style.color = "white";
  btn2.style.backgroundColor = "#56ab2f"; // Correct answer
  btn2.style.color = "white";
  btn3.style.backgroundColor = "#ED213A";

  spark_btn(btn4);
  if (id == "btn1") {
    shake_btn(btn1);
  } else if (id == "btn3") {
    shake_btn(btn3);
  }
  no_click(event);
}
