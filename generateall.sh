for file in ./files/*.rinha; do
    newFileName=${file%.rinha}
    cargo run --manifest-path ../rinha-de-compiler/Cargo.toml \
        ${file} | jq . > "${newFileName}.json"
done;