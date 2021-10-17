module.exports.sendJSONResponse = (res, status, content = null) => {
    res.status(status).json(content);
}

