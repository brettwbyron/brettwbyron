var router = require("/router.js");

import { createServer } from "http";
createServer(function(request, response) {
    router.home(request, response);
    router.page(request, response);
}).listen(3000);