
// Load plugins
var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    cssnano = require('gulp-cssnano'),
    rename = require('gulp-rename'),
    notify = require('gulp-notify'),
    del = require('del'),
    plumber = require('gulp-plumber'),
    browserSync = require('browser-sync'),
    changed = require('gulp-changed');


// Styles
gulp.task('styles', function() {
  return gulp.src('docs/_static/2019/scss/main.scss', { style: 'expanded' })
    .pipe(sass().on('error', sass.logError))
    .pipe(plumber())
    .pipe(autoprefixer({browsers: ['last 2 version']}))
    .pipe(gulp.dest('docs/_static/2019/css/'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(cssnano())
    .pipe(gulp.dest('docs/_static/2019/css/'))
    .pipe(notify({ message: 'Styles task complete' }));
});


// Static server
gulp.task('browser-sync', function() {
    browserSync.init([
      "docs/_static/2019/css/*.css",
      "docs/_static/2019/js/*.js",
      'docs/_templates/2019/*.html'], {
        proxy:  "http://localhost:8888"
    });
});

// Watch
gulp.task('watch', ['browser-sync'], function() {
  gulp.watch('docs/_static/2019/scss/main.scss', ['styles']);
});

// Default task
gulp.task('default', ['browser-sync'], function() {
    gulp.start('styles');
    gulp.start('watch');
});
