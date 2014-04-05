var paper;

var width = 18;
var height = 18;
var start_x = 22;
var start_y = 22;

var seatmap = {
    "rows": {},
    "pk": current_seatmap["pk"]
};

//var seatmap = {
//    rownumber: {
//            orientation: 0,
//            position_x: 0,
//            position_y: 0,
//            seats: {
//                seatnumber: {
//                    status: ""
//                }
//            }
//    }
//}

function dir(object) {
    stuff = [];
    for (s in object) {
        stuff.push(s);
    }
    stuff.sort();
    return stuff;
}

var clearForm = function() {
    $("#amount").val("");
    $("#rownumber").val("");
}

var updateForm = function(seatObject) {
    var row = seatObject.row;
    var pos = row["seatset"][0].getBBox();
    $("#pos_x").text(pos.x);
    $("#pos_y").text(pos.y);
    row.position_x = pos.x;
    row.position_y = pos.y;
}

var removeRow = function() {
    for (var r in seatmap["rows"]) {
        if (seatmap["rows"][r]["selected"]) {
            seatmap["rows"][r]["seatset"].remove();
            delete seatmap["rows"][r];
        }
    }
}

var stripSeatmapCycles = function(sm) {
    var sm2 = jQuery.extend(true, {}, sm);
    for (var r in sm2["rows"]) {
        delete sm2["rows"][r]["seatset"];
    }
    return sm2;
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
        seatmap["rows"][rownumber]["seatset"] = paper.set();
        seatmap["rows"][rownumber]["seats"] = {};
        seatmap["rows"][rownumber]["selected"] = false;

        if (orientation == "0") {
            for (var s = 1; s < (amount/2)+1; s++) {
                var seatx = x + width;
                var seaty = y + s * height;

                var seat = paper.rect(seatx, seaty, width, height);
                    seat.attr({stroke: "#000", 'stroke-width': 2, fill: "#0099FF", opacity: .4});
                var seat2 = paper.rect(seatx+width, seaty, width, height);
                    seat2.attr({stroke: "#000", 'stroke-width': 2, fill: "#0099FF", opacity: .4});
                seat.number = s;
                seat2.number = s + (amount/2);
                seat.row = seatmap["rows"][rownumber];
                seat2.row = seatmap["rows"][rownumber];
                seat.status = (rownumber in current_seatmap["rows"]) ? current_seatmap["rows"][rownumber]["seats"][seat.number].status : 0;
                seat2.status = (rownumber in current_seatmap["rows"]) ? current_seatmap["rows"][rownumber]["seats"][seat2.number].status : 0;;

                //seat.mouseover(function(){
                //});

                //seat.mouseout(function(){
                //    this.attr("opacity", .4);
                //});

                seat.click(clickSeat);
                seat2.click(clickSeat);

                seatmap["rows"][rownumber]["seatset"].push(seat);
                seatmap["rows"][rownumber]["seatset"].push(seat2);
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
                seat.row = seatmap["rows"][rownumber];
                seat2.row = seatmap["rows"][rownumber];
                seat.status = (rownumber in current_seatmap["rows"]) ? current_seatmap["rows"][rownumber]["seats"][seat.number].status : 0;
                seat2.status = (rownumber in current_seatmap["rows"]) ? current_seatmap["rows"][rownumber]["seats"][seat2.number].status : 0;;

                //seat.mouseover(function(){
                //});

                //seat.mouseout(function(){
                //    this.attr("opacity", .4);
                //});

                seat.click(clickSeat);
                seat2.click(clickSeat);

                seatmap["rows"][rownumber]["seatset"].push(seat);
                seatmap["rows"][rownumber]["seatset"].push(seat2);
                seatmap["rows"][rownumber]["seats"][seat.number] = {
                    status: 0
                }
                seatmap["rows"][rownumber]["seats"][seat2.number] = {
                    status: 0
                }
            }

        }


        seatmap["rows"][rownumber]["seatset"].draggable();
        seatmap["rows"][rownumber]["seatset"].click(function() {
            if (!seatmap["rows"][rownumber]["selected"]) {
                for (var r in seatmap["rows"]) {
                    seatmap["rows"][r]["seatset"].attr({opacity:.4});
                    seatmap["rows"][r]["selected"] = false;
                }
                seatmap["rows"][rownumber]["seatset"].attr({opacity:1});
                seatmap["rows"][rownumber]["selected"] = true;
                $("#row-text").text(rownumber);
            } else {
                seatmap["rows"][rownumber]["seatset"].attr({opacity:.4});
                seatmap["rows"][rownumber]["selected"] = false;
                $("#row-text").text("");
            }
        })
    }
}


var createNewRow = function() {
    var amount = parseInt($("#amount").val());
    var x = start_x;
    var y = start_y;
    var orientation = $("#orientation").val();
    var rownumber = parseInt($("#rownumber").val());

    if (rownumber in seatmap["rows"]) {
        alert("The rownumber is not unique!");
        return clearForm();
    }

    createRow(amount, x, y, orientation, rownumber);

};

var clickSeat = function(){
    $("#seat-text").text(this.number);
    if (this.attrs.fill == "#0099FF") {
        this.attr("fill", "#8AE65C");
    } else {
        this.attr("fill", "#0099FF");
    }
}









window.onload = function() {
    paper = Raphael(document.getElementById("seatmap"), seatmap.width, seatmap.height);

    Raphael.st.draggable = function() {
          var me = this,
              lx = 0,
              ly = 0,
              ox = 0,
              oy = 0,
              moveFnc = function(dx, dy) {
                  lx = dx + ox;
                  ly = dy + oy;
                  me.transform('t' + lx + ',' + ly);
                  updateForm(this);
              },
              startFnc = function() {},
              endFnc = function() {
                  ox = lx;
                  oy = ly;
              };

          this.drag(moveFnc, startFnc, endFnc);

        };

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