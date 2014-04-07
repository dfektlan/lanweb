var paper;

var width = 18;
var height = 18;
var start_x = 22;
var start_y = 22;

var seatmap = {
    "rows": {},
    "pk": current_seatmap["pk"]
};

function dir(object) {
    stuff = [];
    for (s in object) {
        stuff.push(s);
    }
    stuff.sort();
    return stuff;
}

$("#save_seatmap").click(function() {
        $.ajax({
        url: '/seatmap/save/',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(stripSeatmapCycles(seatmap)),
        dataType: 'text',
        success: function(result) {
            alert(result.Result);
        }
    })
});


var createRow = function(amount, x, y, orientation, rownumber) {

    if (amount % 2 !== 0) {
        alert("The amount of seats needs to be even");
    } else {
        seatmap["rows"][rownumber] = {}
        seatmap["rows"][rownumber]["orientation"] = orientation;
        seatmap["rows"][rownumber]["position_x"] = x;
        seatmap["rows"][rownumber]["position_y"] = y;
        seatmap["rows"][rownumber]["seats"] = {};

        if (orientation == "0") {
            for (var s = 1; s < (amount/2)+1; s++) {
                var seatx = x + width;
                var seaty = y + s * height;

                var seat = paper.rect(seatx, seaty, width, height);
                var seat2 = paper.rect(seatx+width, seaty, width, height);
                seat.attr({stroke: "#000", 'stroke-width': 2, fill: "#0099FF", opacity: .4});
                seat2.attr({stroke: "#000", 'stroke-width': 2, fill: "#0099FF", opacity: .4});
                seat.number = s;
                seat2.number = s + (amount/2);
                seat.status = (rownumber in current_seatmap["rows"]) ? current_seatmap["rows"][rownumber]["seats"][seat.number].status : 0;
                seat2.status = (rownumber in current_seatmap["rows"]) ? current_seatmap["rows"][rownumber]["seats"][seat2.number].status : 0;;

                //seat.mouseover(function(){
                //});

                //seat.mouseout(function(){
                //    this.attr("opacity", .4);
                //});

                seat.click(clickSeat);
                seat2.click(clickSeat);

                seatmap["rows"][rownumber]["seats"][seat.number] = {
                    status: 0
                }
                seatmap["rows"][rownumber]["seats"][seat2.number] = {
                    status: 0
                }
            }
        } else if (orientation == "1") {
            for (var s = 1; s < (amount/2)+1; s++) {
                var seatx = x + s * width;
                var seaty = y + height;

                var seat = paper.rect(seatx, seaty+height, width, height);
                var seat2 = paper.rect(seatx, seaty, width, height);
                seat.attr({stroke: "#000", 'stroke-width': 2, fill: "#0099FF", opacity: .4});
                seat2.attr({stroke: "#000", 'stroke-width': 2, fill: "#0099FF", opacity: .4});
                seat.number = s;
                seat2.number = s + (amount/2);
                seat.status = (rownumber in current_seatmap["rows"]) ? current_seatmap["rows"][rownumber]["seats"][seat.number].status : 0;
                seat2.status = (rownumber in current_seatmap["rows"]) ? current_seatmap["rows"][rownumber]["seats"][seat2.number].status : 0;;

                //seat.mouseover(function(){
                //});

                //seat.mouseout(function(){
                //    this.attr("opacity", .4);
                //});

                seat.click(clickSeat);
                seat2.click(clickSeat);

                seatmap["rows"][rownumber]["seats"][seat.number] = {
                    status: 0
                }
                seatmap["rows"][rownumber]["seats"][seat2.number] = {
                    status: 0
                }
            }

        }

    }
}


var clickSeat = function(){
    if (this.attrs.fill == "#0099FF") {
        this.attr("fill", "#8AE65C");
    } else {
        this.attr("fill", "#0099FF");
    }
}



window.onload = function() {
    paper = Raphael(document.getElementById("seatmap"), current_seatmap.width, current_seatmap.height);



    var drawExistingSeatMap = function() {

        for (var r in current_seatmap["rows"]) {

            var x = current_seatmap["rows"][r].position_x;
            var y = current_seatmap["rows"][r].position_y;
            var orientation = current_seatmap["rows"][r].orientation;
            var rownumber = r;
            var amount = Object.keys(current_seatmap["rows"][r]["seats"]).length

            createRow(amount, x, y, orientation, rownumber);
        }
    }

    drawExistingSeatMap();



}