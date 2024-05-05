struct Vector {
    x: i32,
    y: i32,
    z: i32,
}
fn main() {
    let mut v1: Vector = Vector {x:1, y:2, z:3};


    println!("Become: v1.x = {}", v1.x);

    inc_x(&mut v1);

    println!("After: v1.x = {}", v1.x);
}


// In Rust is standard Snake Case
fn inc_x(v: &mut Vector) {
    v.x += 1;
}
