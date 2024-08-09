module.exports = {
    apps: [{
      script: "python client/monitor.py",
      watch: ["server", "client"],
      // Delay between restart
      watch_delay: 1000,
      ignore_watch : ["node_modules", "client/img", "\\.git", "*.log"],
    }]
  }