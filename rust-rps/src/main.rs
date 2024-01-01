use rand::Rng;
use std::io;


fn bot_pick() -> &'static str {
    // Generates random number
    let mut rng = rand::thread_rng();
    let random_number: usize = rng.gen_range(0..=2);

    let picks: [&str; 3] = ["Rock", "Paper", "Scissor"];
    let pick: &str = picks[random_number];
    return pick;
}

fn user_pick() -> &'static str {
    println!("Rock[R], Paper[P], or Scissors[S]: ");

    let mut input_raw = String::new();
    io::stdin()
        .read_line(&mut input_raw)
        .expect("Failed to read line");

    let input: &str = input_raw.as_str().trim();

    if input == "R" || input == "r" {
        return "Rock"
    } else if input == "P" || input == "p" {
        return "Paper"
    } else if input == "S" || input == "s" {
        return "Scissor"
    } else {
        return "None"
    }
}

fn calculate_winner(bot: &str, user: &str) -> &'static str {
    println!("{}, {}", bot, user);

    return "yooo"
}

fn main() {
    println!("Hello, world!");
    // println!("bot picked: {}", bot_pick());

    let user_pick = user_pick();
    println!("You picked: {}", user_pick);

    calculate_winner(bot_pick(), user_pick);
}
