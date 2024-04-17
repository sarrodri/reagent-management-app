//look at getElementsByClassName() function for showing the data in the window (index from like 0 to 29)
//call() function in js for search
//import 
function TempSubmitForm(){
    let ClockFaceTime = document.getElementById('ClockFaceTime').value
    let reagent_names = document.getElementById('reagent_names').value
    console.log(ClockFaceTime)
    console.log(reagent_names)
}

 //barcodeIn function will try to find barcodes that are already in the list and information that
 //corresponds to the barcode that is in the list
function barcodeIn() {
    let newBarcode = prompt("Scan Barcode");
    let barcodeFound = false;
    for (let i = 0; i < upc.length; i++) {
        alert("Barcode " + newBarcode + "already exists, corresponds to: " + upc[i].value);
        found = true;
        break;
    }
if (!found) {
    alert("Barcode " + newBarcode + " is not in the list.")
}
}


// The Undo function would be two steps, the Undo would lead to UndoValidation where there would be another prompt before a undoing
function Undo(){
    let UndoPopup = confirm("Are you sure you'd like to undo?")
    if (UndoPopup == true) {
        UndoValidation()
    }
    else {
        return false
    }
}