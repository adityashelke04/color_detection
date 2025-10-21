"""
Comprehensive test script for yellow color detection
Tests all major functionality
"""

import sys
import os


def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    try:
        import cv2
        import numpy as np
        from PIL import Image
        from color_detection import detect_yellow_color, detect_yellow_with_pillow
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def test_dependencies():
    """Test that dependencies are installed correctly"""
    print("\nTesting dependencies...")
    try:
        import cv2
        print(f"  ✓ OpenCV version: {cv2.__version__}")
        
        import numpy as np
        print(f"  ✓ NumPy version: {np.__version__}")
        
        import PIL
        print(f"  ✓ Pillow version: {PIL.__version__}")
        
        return True
    except Exception as e:
        print(f"✗ Dependency error: {e}")
        return False


def test_create_test_images():
    """Test creating test images"""
    print("\nTesting test image creation...")
    try:
        from create_test_image import create_test_image_opencv
        create_test_image_opencv("test_verify.jpg")
        
        if os.path.exists("test_verify.jpg"):
            print("  ✓ Test image created successfully")
            return True
        else:
            print("  ✗ Test image not found")
            return False
    except Exception as e:
        print(f"✗ Error creating test image: {e}")
        return False


def test_yellow_detection():
    """Test yellow color detection"""
    print("\nTesting yellow color detection...")
    try:
        from color_detection import detect_yellow_color
        import cv2
        
        if not os.path.exists("test_verify.jpg"):
            print("  ✗ Test image not found")
            return False
        
        # Run detection
        original, mask, result = detect_yellow_color("test_verify.jpg", "test_verify_output.jpg")
        
        # Verify outputs
        if original is None or mask is None or result is None:
            print("  ✗ Detection returned None values")
            return False
        
        # Check dimensions
        if original.shape != result.shape:
            print("  ✗ Output shape mismatch")
            return False
        
        # Check that some yellow was detected
        yellow_pixels = cv2.countNonZero(mask)
        if yellow_pixels == 0:
            print("  ✗ No yellow pixels detected")
            return False
        
        print(f"  ✓ Detected {yellow_pixels} yellow pixels")
        
        # Verify output file was created
        if not os.path.exists("test_verify_output.jpg"):
            print("  ✗ Output file not created")
            return False
        
        print("  ✓ Yellow detection working correctly")
        return True
        
    except Exception as e:
        print(f"✗ Error in yellow detection: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_pillow_detection():
    """Test Pillow-based detection"""
    print("\nTesting Pillow-based detection...")
    try:
        from color_detection import detect_yellow_with_pillow
        import cv2
        
        if not os.path.exists("test_verify.jpg"):
            print("  ✗ Test image not found")
            return False
        
        original, mask, result = detect_yellow_with_pillow("test_verify.jpg")
        
        if original is None or mask is None or result is None:
            print("  ✗ Detection returned None values")
            return False
        
        yellow_pixels = cv2.countNonZero(mask)
        print(f"  ✓ Pillow detection found {yellow_pixels} yellow pixels")
        return True
        
    except Exception as e:
        print(f"✗ Error in Pillow detection: {e}")
        return False


def cleanup_test_files():
    """Clean up test files"""
    print("\nCleaning up test files...")
    test_files = ["test_verify.jpg", "test_verify_output.jpg"]
    for f in test_files:
        if os.path.exists(f):
            os.remove(f)
            print(f"  ✓ Removed {f}")


def main():
    """Run all tests"""
    print("=" * 60)
    print("Yellow Color Detection - Verification Tests")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("Dependencies", test_dependencies()))
    results.append(("Test Image Creation", test_create_test_images()))
    results.append(("Yellow Detection", test_yellow_detection()))
    results.append(("Pillow Detection", test_pillow_detection()))
    
    # Clean up
    cleanup_test_files()
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name:.<40} {status}")
    
    print("=" * 60)
    print(f"Tests passed: {passed}/{total}")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print(f"\n⚠ {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
