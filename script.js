// script.js
function sortTable(colIndex) {
  const table = document.querySelector('.data-table');
  const rows = Array.from(table.tBodies[0].rows);
  const asc = table.getAttribute('data-sort-asc') === 'true';
  rows.sort((a, b) => {
    const aText = a.cells[colIndex].innerText;
    const bText = b.cells[colIndex].innerText;
    const numA = parseFloat(aText) || aText;
    const numB = parseFloat(bText) || bText;
    return (numA > numB ? 1 : -1) * (asc ? 1 : -1);
  });
  table.setAttribute('data-sort-asc', (!asc).toString());
  rows.forEach(r => table.tBodies[0].appendChild(r));
}
function filterData() {
  alert('You clicked Submit — now hook this up to your back end!');
}
function submitSimilarityRequest() {
  alert('Similarity request submitted — now hook this up!');
}
