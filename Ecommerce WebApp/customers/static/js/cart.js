let updateCart = document.querySelector('.update-cart');
let totalquantity = 0;
let cart_item_number = document.querySelector(".cart-item-number");
for(let i = 0; i<localStorage.length; i++){
    let holder = JSON.parse( localStorage.getItem(localStorage.key(i)) )
    if(holder == true){
        continue;
    }
    else{
        console.log("HOLDER "+holder.quantity)
        totalquantity = totalquantity + Number(holder.quantity)
        console.log("TOTAL VALUE    "+totalquantity)
        cart_item_number.innerHTML = totalquantity
    }
}

// function ClearStorage(){
//     for(let i=0; i<localStorage.length; i++){
//         if(localStorage.key(i).slice(0,4) == "user"){
//             localStorage.removeItem(localStorage.key(i))
//         }
//     }
// }

function ClearStorage(){
    localStorage.clear()
}


// updateCart.addEventListener('click',function(){
//     var productId = this.dataset.product
//     var action = this.dataset.action
//     console.log('productId: ',productId,'action: ',action)
// })

function ActionPerformed(val){
    let id = val.getAttribute("data-product")
    let action = val.getAttribute("data-action")
    
    

    //ADDING ITEM ACTION
    if(action == "add"){
        let quantity = document.querySelector('.ord-num').value;
        console.log(id,quantity)
        
        if(localStorage.getItem("user:"+id)){
            let x = localStorage.getItem("user:"+id)
            prod = JSON.parse(x)
            prodquant = prod.quantity
            prodquant = Number(prodquant)
            prodd = Number(quantity) + prodquant
            prod.quantity = prodd

            localStorage.setItem("user:"+id, JSON.stringify(prod))
        }
        else{
            const prodinfo = {
                id: id,
                quantity:quantity
            }
            localStorage.setItem("user:"+id, JSON.stringify(prodinfo))
        }
    }
    else if(action == "remove"){
        console.log("THE ACTION IS TO REMOVE OBJECTS")
        let quantity = val.getAttribute("data-quantity")
        if(localStorage.getItem("user:"+id)){
            let x = localStorage.getItem("user:"+id)
            prod = JSON.parse(x)
            prodquant = prod.quantity
            prodquant = Number(prodquant)
            if(prodquant > 0){
                prodd =  prodquant - Number(quantity)
                prod.quantity = prodd

                localStorage.setItem("user:"+id, JSON.stringify(prod))
            }
            else{
                alert("The item quantity is now zero")
            }
        }
        else{
            console.log("ITEM IS NOT IN LOCAL STORAGE.")
        }
    }
}