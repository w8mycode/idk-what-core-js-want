const dataContainer = document.querySelector('.data-container');
const searchInput = document.querySelector('#search');
lines = [];

searchInput.addEventListener('input', (e) => {
  const value = e.target.value.toLowerCase();
  lines.forEach((line) => {
    const text = line.innerHTML.toLowerCase();
    isVisible = () => !text.includes(value);
    line.classList.toggle('hide', isVisible());
  });
});

fetch('/data/data.json')
  .then((res) => res.json())
  .then((data) => {
    for (let [key, value] of Object.entries(data)) {
      const tr = document.createElement('tr');
      const td1 = document.createElement('td');
      const td2 = document.createElement('td');
      td1.innerText = key;
      td2.innerText = value;
      tr.append(td1);
      tr.append(td2);
      dataContainer.append(tr);
      lines.push(tr);
    }
  });

searchInput.focus();
