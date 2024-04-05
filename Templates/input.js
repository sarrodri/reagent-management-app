//look at getElementsByClassName() function for showing the data in the window (index from like 0 to 29)
//call() function in js for search
//import
function TempSubmitForm(){
    let ClockFaceTime = document.getElementById('ClockFaceTime').value
    let reagent_names = document.getElementById('reagent_names').value
    console.log(ClockFaceTime)
    console.log(reagent_names)
}

function barcodeIn() {
    let newBarcode = prompt("Scan Barcode");
    //if newBarcode in barcodeList{
      //show what it is
    //}
}

function SubmitForm(){

}

// The Undo function would be two steps, the Undo would lead to UndoValidation where there would be another prompt before a undoing
function Undo(){
    let UndoPopup = confirm("Are you sure you'd like to undo?")
    if (UndoPopup == true) {
        UndoValidation()
    }
    else {
        null
    }
}

function UndoValidation(){
    
}

function getReagentNames(reagent_names){
    reagent_names
}