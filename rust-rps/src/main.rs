use rand::Rng;
use std::io::{stdin, stdout, Write};


fn bot_pick() -> &'static str {
    // Generates random number
    let mut rng = rand::thread_rng();
    let random_number: usize = rng.gen_range(0..=2);

    let picks: [&str; 3] = ["Rock", "Paper", "Scissor"];
    let pick: &str = picks[random_number];
    return pick;
}

fn user_pick() -> String {
    let mut input = String::new();
    print!("Rock[R], Paper[P], or Scissors[S]: ");
    let _ = stdout().flush();
    stdin().read_line(&mut input).expect("Failed to read line");
    println!("You entered: {}", input.trim());
    return input
}

fn main() {
    println!("Hello, world!");
    println!("{}", bot_pick());
    user_pick();
}
