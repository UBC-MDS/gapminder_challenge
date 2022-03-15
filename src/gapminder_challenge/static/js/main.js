function flip(event) {
  var element = event.currentTarget.closest(".card");
  if (element.style.transform == "rotateY(180deg)") {
    element.style.transform = "rotateY(0deg)";
  }
  else {
    element.style.transform = "rotateY(180deg)";
  }
};

function flip_story(event) {
  var element = event.currentTarget.closest(".card");
     var front = element.querySelector('.front');
    var story = element.querySelector('.story');
    if (element.style.transform == "rotateY(180deg)") {
      front.style.display = "none";
      story.style.display = "block";

      // var myVizzu = document.getElementById("myVizzu");
      var myVizzu = event.currentTarget.closest(".card");
      myVizzu.style.width = '650px';
      myVizzu.style.height = '500px';

      element.style.transform = "rotateY(360deg)";
      drawBarChart(event);
    }
    else {
      element.style.transform = "rotateY(180deg)";
      setTimeout(() => {  
        front.style.display = "flex"; 
        story.style.display = "none";
      }, 1000);
    }
};

function spark_btn(btn) {
  setTimeout(function () {
    btn.style.display = "block"
    btn.classList.add('is-active');
    party.sparkles(btn);
  }, 1500);
}
function shake_btn(btn) {
  btn.classList.add("button-shake");
}

function no_click(event) {
  var element = event.currentTarget.closest(".btn-group");
  element.classList.add("no-click");
}

function quiz1Func(event, id) {

  btn1 = document.getElementById("btn1");
  btn2 = document.getElementById("btn2");
  btn3 = document.getElementById("btn3");
  btn4 = document.getElementById("btn4");

  btn1.style.backgroundColor = "#ED213A";
  btn1.style.color = "white";
  btn2.style.backgroundColor = "#56ab2f";    // correct answer
  btn2.style.color = "white";
  btn3.style.backgroundColor = "#ED213A";
  btn3.style.color = "white";

  spark_btn(btn4);
  if (id == 'btn1') {
    shake_btn(btn1);
  }
  else if (id == 'btn3') {
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
  btn3.style.backgroundColor = "#56ab2f";  // correct answer is 2.7
  btn3.style.color = "white";

  spark_btn(btn4);
  if (id == 'btn1') {
    shake_btn(btn1);
  }
  else if (id == 'btn2') {
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
  btn3.style.backgroundColor = "#56ab2f";  // correct answer is 2.7
  btn3.style.color = "white";

  spark_btn(btn4);
  if (id == 'btn1') {
    shake_btn(btn1);
  }
  else if (id == 'btn2') {
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
  btn2.style.backgroundColor = "#56ab2f";// Correct answer
  btn2.style.color = "white";
  btn3.style.backgroundColor = "#ED213A";

  spark_btn(btn4);
  if (id == 'btn1') {
    shake_btn(btn1);
  }
  else if (id == 'btn3') {
    shake_btn(btn3);
  }
  no_click(event);

}