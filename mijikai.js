function convert() {
    var inputText = document.getElementById("t1").value;
    var summary = generateSummary(inputText);
    document.getElementById("t2").value = summary;
    // document.getElementById("downloadLink").setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(summary));
    // document.getElementById("downloadLink").setAttribute("download", "summary.txt");
    // document.getElementById("downloadLink").style.display = "block";
}

function generateSummary(text) {
    
    return text;
} 
