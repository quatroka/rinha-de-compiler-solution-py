for file in ./files/*.rinha; do
    cargo run --manifest-path ../rinha-de-compiler/Cargo.toml \
        ${file} | jq . > ${file}.json
done;