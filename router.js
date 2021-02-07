function home(request, response) {
    if(request.url === "/") {
        response.writeHead(200, {'Content-Type': 'text/plain'});
        response.write("test\n");
        response.end("end\n");
    }
}

function page(request, response) {
    var route = request.url.replace("/","");
    if(route.length > 0) {
        response.write('new\n');
        response.end("end\n");
    }
}

module.exports.home = home;
module.exports.page = page;