const { sendJSONResponse } = require('../common')
const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args));
let counter = 0

module.exports.findOne = async (req, res) => {
    try {
        let ans = await findSome(req.query.inn)
        res.send(ans)
        counter += 1
        console.log(`Отдал ${counter}`);
    }
    catch (err) {
        console.log(err.message)
        sendJSONResponse(res, 500)
    }
}

async function findSome(param) {
    var url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party";
    var token = "d9474f76262e319098db5615122459f330769067";
    var query = param;
    var options = {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + token
        },
        body: JSON.stringify({ query: query })
    }
    var ans = {}
    await fetch(url, options)
        .then(response => response.text())
        .then(result => ans = result)
        .catch(error => console.log("error", error));
    return ans
}