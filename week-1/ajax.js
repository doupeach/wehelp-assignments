// function ajax(src, callback) {
//   // your code here
//   var xhr = new XMLHttpRequest();
//   xhr.open(
//     "GET",
//     "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json",
//     true
//   );
//   xhr.onreadystatechange = function () {
//     if (xhr.readyState === 4 && xhr.status === 200) {
//       let res = JSON.parse(xhr.responseText);
//       console.log(res);
//       let data = res.result.results;
//       console.log(data);
//       // render(res);
//     }
//   };
//   xhr.send();
// }

const ajax = (url) => {
  fetch(url, {
    method: "GET",
  })
    .then((res) => res.json())
    .then((res) => {
      render(res);
    });
};

function render(res) {
    const cardsDiv = document.createElement("div");
    for (let key = 0; key < 8; key++) {
        data = res.result.results
        cardsDiv.className = "cards";
        const wrap = document.createElement("div");
        wrap.className = "card";
        const image = document.createElement("img");
        const title = document.createElement("div");
      imageSrc = data[key].file.split('.jpg')[0];
      image.src = `${imageSrc}.jpg`
      title.textContent = data[key].stitle;
      wrap.appendChild(image);
      wrap.appendChild(title);
      cardsDiv.appendChild(wrap);
    }
    document.getElementById("cards-container").appendChild(cardsDiv);

  }


ajax(
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
);
