"""Unit tests for the Evolution of Todo project setup."""
import sys
import importlib.util


def test_basic_imports():
    """Test that basic modules can be imported."""
    try:
        # Test that the main module can be imported
        spec = importlib.util.spec_from_file_location("main", "src/main.py")
        main_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_module)
        print("✓ Main module imports successfully")

        # Test that packages can be imported
        import src
        import src.models
        import src.services
        import src.ui
        print("✓ All packages import successfully")

        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    print("Running basic project setup tests...")
    success = test_basic_imports()

    if success:
        print("\n✓ All basic tests passed!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed!")
        sys.exit(1)