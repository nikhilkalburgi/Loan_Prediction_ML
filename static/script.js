let sib_1 = document.querySelectorAll('.show-in-btn > ul');
let sib_2 = document.querySelectorAll('.show-in-btn > button');
let csv_file = document.getElementsByClassName('csv-file');
let form_control = document.getElementsByClassName('form-control');
let arrow_1 = document.getElementsByClassName('arrow-1');
let graph_btn = document.getElementById('graph-btn');
let btn_y = document.getElementById('btn-y');
let btn_y_ul = document.getElementById('btn-y-ul');
let btn_x = document.getElementById('btn-x');
let processing = document.getElementById('processing');
let graph = document.getElementById('graph');
let graph_btn_ul = document.getElementById('graph-btn-ul');
let btn_z = document.getElementById('btn-z');
let model = document.getElementById('model');
let result = document.getElementsByClassName('result');
let model_btn = document.getElementById('model-btn');
let iv = document.querySelector('.prediction input');
let predict_btn = document.querySelector('.prediction button');
let dialog = document.getElementById('dialog');
let pp = document.getElementsByClassName('pp')

arrow_1[0].style.opacity = 0;
sib_1.forEach((value,index)=>{
    value.onclick = (ev)=>{
        sib_2[index].innerText = ev.target.innerText + '\t\t';

    }
})

graph_btn_ul.onclick=(ev)=>{
    graph_btn.innerText = ev.target.innerText
    if (graph_btn.innerText == 'Pair Plot' || graph_btn.innerText == 'Heat Map'){
        btn_x.classList.add('disabled');
        btn_y.classList.add('disabled');
        graph.innerHTML = '<div class="text-center mt-5 pt-4">\
            <div class="spinner-border" role="status" style="font-size: 3vh;padding: 35px;">\
            </div>\
            <div class="sr-only mt-5" style="font-size: 3vh;">...Just a Second...</div>\
        </div>';
        fetch('/plot', {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify({type:graph_btn.innerText}),
        }).then((resp)=>resp.text())
        .then(data=>{
    
            if(data != "0"){
                window.scroll(0,1800)
                graph.innerHTML = data;
    
            }else{
                dialog.click()
            }
        })
    }else if(graph_btn.innerText == 'Count Plot'){
        btn_x.classList.add('disabled');
        if (btn_y.classList.contains('disabled'))
            btn_y.classList.remove('disabled');
    }else{
        if (btn_x.classList.contains('disabled'))
            btn_x.classList.remove('disabled');
        if (btn_y.classList.contains('disabled'))
            btn_y.classList.remove('disabled');
    } 

    if(graph_btn.innerText == 'Scatter Plot' || graph_btn.innerText == 'Bar Plot' || graph_btn.innerText == 'Count Plot'){
        if (btn_z.classList.contains('disabled'))
            btn_z.classList.remove('disabled');
    }else{
        btn_z.classList.add('disabled');
    }

}

btn_y_ul.onclick=(ev)=>{
    btn_y.innerText = ev.target.innerText
    graph.innerHTML = '<div class="text-center mt-5 pt-4">\
    <div class="spinner-border" role="status" style="font-size: 3vh;padding: 35px;">\
    </div>\
    <div class="sr-only mt-5" style="font-size: 3vh;">...Just a Second...</div>\
  </div>';
    fetch('/plot', {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify({type:graph_btn.innerText,x:btn_x.innerText,y:btn_y.innerText,hue:(btn_z.innerText == 'hue')? "Loan_Status" : btn_z.innerText}),
    }).then((resp)=>resp.text())
    .then(data=>{
        if(data != "0"){
            window.scroll(0,1800)
            graph.innerHTML = data;
            
        }else{
            console.log(data)
            dialog.click()
        }
    })
}

csv_file[0].onclick = (ev)=>{
    console.log( document.getElementsByClassName('arrow-1')[0].style)
    
    fetch('/filepath', {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(form_control[0].value),
    }).then((resp)=>resp.text())
    .then(data=>{
        
        console.log(data)
        if(data != "0"){
            window.scroll(0,600)
            console.log(data)
            arrow_1[0].style.opacity = 1;
            data = JSON.parse(data)
            setTimeout(()=>{processing.innerHTML = data.head + "<h5 class='m-2'> Shape Before : "+data.prevshape+"</h5>" +  "<h5> Shape Now : "+data.shape+"</h5>";},2000)
            

        }else{
            dialog.click()
        }
    })
}

processing.onclick = ()=>{
    if(processing.childElementCount !== 1)
    window.scroll(0,1600);
}

graph.onclick=()=>{
    window.scroll(0,2800);
}
result[0].onclick=()=>{
    document.body.classList.remove("overflow-hidden")
    window.scrollTo(0, document.body.scrollHeight);
}

model.onclick=(ev)=>{
    model_btn.innerText = ev.target.innerText;
    result[0].innerHTML = '<div class="text-center mt-5 pt-4">\
    <div class="spinner-border" role="status" style="font-size: 3vh;padding: 35px;">\
    </div>\
    <div class="sr-only mt-5" style="font-size: 3vh;">...Just a Second...</div>\
  </div>';
    fetch('/model', {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(model_btn.innerText)
    }).then((resp)=>resp.text())
    .then(data=>{
        if(data != "0"){
            window.scroll(0,3100)
            metric = JSON.parse(data)
            result[0].innerHTML = "<pre>"+metric.classification_report+"</pre><hr><pre> Accuracy Score : "+metric.accuracy_score+"</pre>";

        }else{
            dialog.click()
        }
    })
}

predict_btn.onclick = ()=>{
    fetch('/pp', {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(iv.value)
    }).then((resp)=>resp.text())
    .then(data=>{
        if(data != "0"){
            pp[0].innerHTML = "Loan Status : ".concat((data[1] == "1") ? "Yes" : "No");

        }else{
            dialog.click()
        }
    })
}