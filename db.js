const MongoClient = require("mongodb").MongoClient;
const ObjectID = require('mongodb').ObjectID;
const dbname = "ewb_asu";
const url = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.70xfj.mongodb.net/ewb-asu?retryWrites=true&w=majority";
const mongoOptions = {
    useNewUrlParser:true,
    useUnifiedTopology: true // added this
};

const state = {
    db : null
}

const connect = (cb) =>{
    if (state.db)
        cb();
    else {
        MongoClient.connect(url, mongoOptions, (err, client)=>{
            if (err)
                cb(err);
            else {
                state.db = client.db(dbname);
                cb();
            }
        })
    }
}

const getPrimaryKey = (_id)=>{
    return ObjectID(_id); // check this line
}

const getDB = ()=>{
    return state.db;
}

module.exports = {getDB, connect, getPrimaryKey};