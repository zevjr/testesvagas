withenv () {
  env_file="$1"
  cmd="${@:2}"
  bash -c "source $env_file && $cmd"
}
