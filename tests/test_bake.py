def test_bake_project(cookies):
    result = cookies.bake(extra_context={})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "quality_standard_demo"
    assert result.project_path.is_dir()
