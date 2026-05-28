---
name: Runner._add_initial_program
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._add_initial_program

**File:** `skydiscover/runner.py:238`  
**Kind:** method  
**Layer:** #runner

## What it does
Evaluates the initial program and adds it to the database with score 0 (or its real score if evaluation succeeds). This seeds the database so the first iteration has a parent to work from.

## Source
````python
    async def _add_initial_program(self, start_iteration: int) -> None:
        logger.info("Adding initial program to database")
        program_id = str(uuid.uuid4())

        initial_image_path = None
        if self.config.language == "image":
            logger.info("Generating initial image from seed text...")
            img_dir = os.path.join(self.output_dir, "generated_images")
            try:
                result = await self.discovery_controller.llms.generate(
                    system_message="Generate an image based on the following description. Also provide brief reasoning about your creative choices.",
                    messages=[{"role": "user", "content": self.initial_program_solution}],
                    image_output=True,
                    output_dir=img_dir,
                    program_id=program_id,
                )
                initial_image_path = result.image_path
                logger.info(f"Initial image: {initial_image_path}")
            except Exception as e:
                logger.warning(f"Failed to generate initial image: {e}")

        eval_input = (
            initial_image_path
            if self.config.language == "image" and initial_image_path
            else self.initial_program_solution
        )
        eval_result = await self.discovery_controller.evaluator.evaluate_program(
            eval_input, program_id
        )
        metrics = eval_result.metrics

        if not initial_image_path and isinstance(metrics.get("image_path"), str):
            initial_image_path = metrics.pop("image_path")

        program = get_program(
            self.config, self.initial_program_solution, program_id, metrics, start_iteration
        )
        program.artifacts = eval_result.artifacts

        if initial_image_path:
            program.metadata = program.metadata or {}
            program.metadata["image_path"] = initial_image_path

        self.database.add(program)
        try:
            self.database.initial_program_id = program.id
            self.database.initial_program_score = get_score(program.metrics or {})
        except Exception as e:
            logger.warning(f"Failed to set initial program score: {e}")
````

## → Calls
- [[Config.evaluator]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[EvaluationResult.metrics]]
- [[Program.id]]
- [[Program.metadata]]
- [[Program.metrics]]
- [[ProgramDatabase.add]]
- [[Runner.run]]
- [[SearchConfig.output_dir]]
- [[UnifiedArchive.add]]
- [[metrics.get_score]]
- [[registry.create_database]]
- [[registry.get_program]]

## ← Called by
- [[Runner.run]]
