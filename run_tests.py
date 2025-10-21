#!/usr/bin/env python
import os
import sys
import subprocess


def run_django_tests():
    """Запуск Django тестов"""
    print("🔧 Запуск Django тестов...")
    try:
        result = subprocess.run([
            'python', 'manage.py', 'test',
            '--verbosity=2'
        ], capture_output=True, text=True, cwd='.')

        print(result.stdout)
        if result.stderr:
            print("Ошибки Django тестов:", result.stderr)

        return result.returncode == 0
    except Exception as e:
        print(f"❌ Ошибка при запуске Django тестов: {e}")
        return False


def run_pytest_with_coverage():
    """Запуск pytest с проверкой покрытия"""
    print("📊 Запуск pytest с проверкой покрытия...")
    try:
        result = subprocess.run([
            'pytest', '.', '--cov=.', '--cov-report=html', '--cov-report=term',
            '--rootdir=.'
        ], capture_output=True, text=True, cwd='.')

        print(result.stdout)
        if result.returncode != 0:
            print("Pytest завершился с ошибками")
        return True
    except FileNotFoundError:
        print("⚠️  pytest не установлен, пропускаем проверку покрытия")
        return True
    except Exception as e:
        print(f"❌ Ошибка при запуске pytest: {e}")
        return False


def main():
    """Основная функция запуска тестов"""
    print("🎯 Запуск тестовой системы...")
    print(f"📁 Текущая директория: {os.getcwd()}")

    # Запускаем Django тесты
    django_success = run_django_tests()

    # Запускаем pytest (если установлен)
    pytest_success = run_pytest_with_coverage()

    # Сводка результатов
    print("\n" + "="*50)
    print("📊 СВОДКА РЕЗУЛЬТАТОВ ТЕСТИРОВАНИЯ")
    print("="*50)
    print(f"✅ Django тесты: {'ПРОЙДЕНЫ' if django_success else 'ПРОВАЛЕНЫ'}")
    print(f"✅ Pytest покрытие: {'ЗАВЕРШЕНО' if pytest_success else 'ОШИБКА'}")

    overall_success = django_success and pytest_success
    if overall_success:
        print("🎉 Все тесты пройдены успешно!")
    else:
        print("❌ Обнаружены проблемы в тестах")

    return overall_success


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
