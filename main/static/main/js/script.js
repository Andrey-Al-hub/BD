var operation_button = document.querySelector("#operation_confirm_button");
operation_button.addEventListener("click", operationPrint);

var operation_select = document.getElementById("operation_selector");
function operationPrint() {
    var blocks = document.getElementsByClassName("operation");
    for (let i = 0; i < blocks.length; i += 1) {
        blocks[i].style.display = 'none';
    }
    var text = operation_select.options[operation_select.selectedIndex].text;
    if (text == "Приход товара") {
        productIncome();
    }
    if (text == "Списание товара") {
        productWriteOff();
    }
}

// ПРИХОД ТОВАРА
function productIncome() {
    var operation_block = document.getElementsByClassName("operation")[0];
    var income_block = document.getElementById("income_value");
    var new_income_block = document.getElementById("new_income_value");
    var income_select = document.querySelector("#income_selector");
    if (operation_block.style.display == 'none') {
        income_block.style.display = 'none';
        new_income_block.style.display = 'none';
    }
    operation_block.style.display = 'flex';
    income_select.addEventListener('change', productIncomeSelect)
}

function productIncomeSelect() {
    var income_select = document.querySelector("#income_selector");
    text = income_select.options[income_select.selectedIndex].text;
    var income_block = document.getElementById("income_value");
    var new_income_block = document.getElementById("new_income_value");
    if (text != "Выберите товар") {
        if (text == "Добавить новый товар...") {
            income_block.style.display = 'none';
            new_income_block.style.display = 'flex';
            var manufacturer_select = document.getElementById("income_manufacturer");
            manufacturer_select.addEventListener('change', function(){
                var manufacturer = manufacturer_select.options[manufacturer_select.selectedIndex].text;
                if (manufacturer == "Новый производитель...") {
                    document.getElementById("new_manufacturer").style.display = 'flex';
                    document.getElementsByName('new_manufacturer')[0].required = true;
                    document.getElementById("new_manufacturer_city").style.display = 'flex';
                    document.getElementsByName('new_manufacturer_city')[0].required = true;
                }
                else {
                    document.getElementsByName('new_manufacturer')[0].required = false;
                    document.getElementById("new_manufacturer").style.display = 'none';
                    document.getElementsByName('new_manufacturer_city')[0].required = false;
                    document.getElementById("new_manufacturer_city").style.display = 'none';
                }
            })
        }
        else {
            new_income_block.style.display = 'none';
            income_block.style.display = 'flex';
            var income_title = document.getElementsByName('income_title')[0];
            income_title.value = text;
        }
    }
    else {
        income_block.style.display = 'none';
        new_income_block.style.display = 'none';
    }
}


// СПИСАНИЕ ТОВАРА
function productWriteOff() {
    var operation_block = document.getElementsByClassName("operation")[1];
    var write_off_select = document.querySelector("#write_off_selector");
    var write_off_block = document.getElementById("write_off_value");
    if (operation_block.style.display == 'none') {
        write_off_block.style.display = 'none';
    }
    operation_block.style.display = 'flex';
    write_off_select.addEventListener('change', function(){
        var write_off_select = document.querySelector("#write_off_selector");
        text = write_off_select.options[write_off_select.selectedIndex].text;
        var write_off_block = document.getElementById("write_off_value");
        if (text != "Выберите товар") {
            write_off_block.style.display = 'flex';
        }
        else{
            write_off_block.style.display = 'none';
        }
    })
}


