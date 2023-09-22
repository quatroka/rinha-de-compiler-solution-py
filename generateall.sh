for file in ./files/rinha_examples/*.rinha; do
    cargo run --manifest-path ../rinha-de-compiler/Cargo.toml \
        ${file} | jq . > "${file}.json"
done;

for file in ./files/generated_by_me/*.rinha; do
    cargo run --manifest-path ../rinha-de-compiler/Cargo.toml \
        ${file} | jq . > "${file}.json"
done;