---
name: monitor.start_monitor
description: function in skydiscover/extras/monitor/__init__.py (monitor)
metadata:
  type: project
---

# monitor.start_monitor

**File:** `skydiscover/extras/monitor/__init__.py:28`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def start_monitor(
    config, output_dir: str
) -> Tuple[Optional[MonitorServer], Optional[object], Optional[object]]:
    """Start the live monitor server. Returns (server, callback, feedback_reader)."""
    monitor_server = None
    monitor_callback = None
    feedback_reader = None

    if not config.monitor.enabled:
        return monitor_server, monitor_callback, feedback_reader

    try:
        monitor_server = MonitorServer(
            host=config.monitor.host,
            port=config.monitor.port,
            max_solution_length=config.monitor.max_solution_length,
        )
        monitor_server.start()
        monitor_callback = create_external_callback(monitor_server, time.time())

        if config.monitor.summary_model:
            monitor_server.configure_summary(
                model=config.monitor.summary_model,
                api_key=config.monitor.summary_api_key or "",
                api_base=config.monitor.summary_api_base,
                top_k=config.monitor.summary_top_k,
                interval=config.monitor.summary_interval,
            )

        try:
            from skydiscover.context_builder.human_feedback import HumanFeedbackReader

            feedback_path = getattr(config, "human_feedback_file", None) or os.path.join(
                output_dir, "human_feedback.md"
            )
            feedback_mode = getattr(config, "human_feedback_mode", "append")
            feedback_reader = HumanFeedbackReader(feedback_path, mode=feedback_mode)
            monitor_server.set_feedback_reader(feedback_reader)
            logger.info("Human feedback enabled — file: %s", feedback_path)
        except Exception as exc:
            logger.warning("Failed to set up human feedback: %s", exc)

        url = f"http://localhost:{monitor_server.port}/"
        print(f"\n  Live monitor: {url}\n", flush=True)
        logger.info("Live monitor: %s", url)

    except Exception as exc:
        logger.warning("Failed to start monitor: %s", exc)

    return monitor_server, monitor_callback, feedback_reader
````

## → Calls
- [[Config.monitor]]
- [[HumanFeedbackReader.__init__]]
- [[MonitorConfig.port]]
- [[MonitorServer.__init__]]
- [[MonitorServer.configure_summary]]
- [[MonitorServer.set_feedback_reader]]
- [[MonitorServer.start]]
- [[callback.create_external_callback]]
- [[human_feedback.HumanFeedbackReader]]
- [[server.MonitorServer]]

## ← Called by
- [[api._run_discovery_async]]
- [[cli.main_async]]
