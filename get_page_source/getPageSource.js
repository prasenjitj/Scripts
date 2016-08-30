function DOMtoString(document_root) {
    if(document.URL =="http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena"){
    var title =document.getElementsByTagName("title")[0].innerText;
    console.log(title);
    var prize_category = document.getElementsByClassName("related-box")[0].getElementsByTagName("strong");
    var winners = document.getElementsByClassName("related-box")[0].getElementsByTagName("p");
    
    // console.log(prize_category);
   for (var i =0;i<3;i++){
    console.log(prize_category[i].innerText.replace(/\s.*/,""));
    if(winners[i].innerText.match(/(.*)\sapostas/ig)!=undefined){
    console.log(winners[i].innerText.match(/(.*)\sapostas/ig)[0].replace(/\sapostas/,""));
    console.log(winners[i].innerText.match(/R\$\s(.*)/)[1]);
    console.log(document.URL);

    }
}

}
else {console.log("wrong page")}    

}
chrome.runtime.sendMessage({
    action: "getSource",
    source: DOMtoString(document)
});
