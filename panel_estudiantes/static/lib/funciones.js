function toggleTable(grado) {
    var table = document.getElementById(grado);
    if (table.style.display === "none") {
        table.style.display = "block";
    } else {
        table.style.display = "none";
    }
}