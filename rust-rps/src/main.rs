use rand::Rng;


fn bot_pick() -> &'static str {
    // Generates random number
    let mut rng = rand::thread_rng();
    let random_number: usize = rng.gen_range(0..=2);

    let picks: [&str; 3] = ["Rock", "Paper", "Scissor"];
    let pick: &str = picks[random_number];
    return pick;
}

fn main() {
    println!("Hello, world!");
    println!("{}", bot_pick());
}
