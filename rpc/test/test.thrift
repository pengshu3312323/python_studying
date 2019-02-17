// test thrift

struct Result {
    1:bool success;
    2:string msg;
}

service Test {
    Result echo(1:string msg, 2:i64 delay);
}
